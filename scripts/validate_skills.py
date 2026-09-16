#!/usr/bin/env python3
"""Validate metadata, local references, standalone packaging, and catalog coverage."""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

import yaml

from sync_shared import ROOT, sync


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject duplicate mapping keys rather than silently losing metadata."""


def unique_mapping(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ValueError(f"Duplicate YAML key: {key}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def read_yaml(text):
    value = yaml.load(text, Loader=UniqueKeyLoader)
    if not isinstance(value, dict):
        raise ValueError("Expected a YAML mapping")
    return value


def validate(root=ROOT):
    errors = []
    skills = sorted((root / "skills").glob("*/SKILL.md"))
    if not skills:
        return ["No skills found"]
    names = set()
    for entry in skills:
        base = entry.parent
        label = str(base.relative_to(root))
        names.add(base.name)
        try:
            text = entry.read_text()
            parts = re.fullmatch(r"---\r?\n(.*?)\r?\n---(?:\r?\n|$)(.*)", text, re.DOTALL)
            if not parts:
                raise ValueError("Missing YAML frontmatter")
            metadata = read_yaml(parts[1])
            if metadata.get("name") != base.name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", base.name):
                raise ValueError("Name must match its kebab-case directory")
            if len(base.name) > 64:
                raise ValueError("Name exceeds 64 characters")
            description = metadata.get("description")
            if not isinstance(description, str) or not description.strip() or len(description) > 1024:
                raise ValueError("Description must be nonempty and at most 1024 characters")
            if not parts[2].strip():
                raise ValueError("Skill body is empty")
            agent = read_yaml((base / "agents/openai.yaml").read_text())
            interface = agent["interface"]
            if not isinstance(interface, dict):
                raise ValueError("Expected interface to be a mapping")
            for key in ("display_name", "short_description", "default_prompt"):
                if not isinstance(interface.get(key), str) or not interface[key].strip():
                    raise ValueError(f"Missing interface.{key}")
            if not 25 <= len(interface["short_description"]) <= 64:
                raise ValueError("UI short description must have 25 to 64 characters")
            if f"${base.name}" not in interface["default_prompt"]:
                raise ValueError("Default prompt must invoke this skill")
            policy = agent.get("policy", {})
            if not isinstance(policy, dict) or policy.get("allow_implicit_invocation") is not True:
                raise ValueError("This catalog preserves automatic invocation")
        except (OSError, ValueError, KeyError, TypeError, yaml.YAMLError) as exc:
            errors.append(f"{label}: {exc}")
        for file in base.rglob("*"):
            if file.is_symlink():
                errors.append(f"{file.relative_to(root)}: symlinks break independent packaging")
        for file in base.rglob("*.md"):
            if file.is_symlink():
                continue
            for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", file.read_text()):
                target = link.strip().strip("<>")
                parsed = urlsplit(target)
                if parsed.scheme in {"https", "http", "mailto"}:
                    continue
                if parsed.scheme or target.startswith("/"):
                    errors.append(f"{file.relative_to(root)}: nonportable link {target}")
                    continue
                if not parsed.path:
                    continue
                path = (file.parent / unquote(parsed.path)).resolve()
                if not path.is_relative_to(base.resolve()):
                    errors.append(f"{file.relative_to(root)}: link escapes skill: {target}")
                elif not path.exists():
                    errors.append(f"{file.relative_to(root)}: missing link: {target}")
    for path in sync(root, check=True):
        errors.append(f"Shared reference drift: {path}")
    try:
        catalog = json.loads((root / "docs/catalog.json").read_text())
        catalog_names = [item["name"] for item in catalog]
        if len(set(catalog_names)) != len(catalog_names) or set(catalog_names) != names:
            errors.append("Catalog must list each skill exactly once")
        readme = (root / "README.md").read_text()
        for name in names:
            if f"skills/{name}/SKILL.md" not in readme:
                errors.append(f"README does not link to {name}")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f"Catalog/README: {exc}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    errors = validate(args.root.resolve())
    for error in errors:
        print(f"ERROR: {error}")
    if not errors:
        print(f"Validated {len(list((args.root / 'skills').glob('*/SKILL.md')))} standalone skills.")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
