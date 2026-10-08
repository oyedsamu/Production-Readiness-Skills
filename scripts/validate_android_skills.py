#!/usr/bin/env python3
"""Validate the separate Android starter package without changing catalog rules."""
import argparse
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

from validate_skills import read_yaml
import yaml

ROOT = Path(__file__).resolve().parents[1] / 'flamong-android-engineering'


def validate(root=ROOT):
    root = root.resolve()
    errors = []
    entries = sorted((root / 'skills').glob('*/SKILL.md'))
    if not entries:
        errors.append('No Android skills found')
    names = set()
    for directory in sorted((root / 'skills').iterdir()) if (root / 'skills').is_dir() else []:
        if directory.is_dir() and not (directory / 'SKILL.md').is_file():
            errors.append(f'{directory.name}: missing SKILL.md')
    for entry in entries:
        label = entry.relative_to(root)
        names.add(entry.parent.name)
        try:
            text = entry.read_text(encoding='utf-8')
            parts = re.fullmatch(r'---\r?\n(.*?)\r?\n---(?:\r?\n|$)(.*)', text, re.DOTALL)
            if not parts:
                raise ValueError('Missing YAML frontmatter')
            metadata = read_yaml(parts[1])
            name = metadata.get('name')
            if name != entry.parent.name or not re.fullmatch(r'android-[a-z0-9]+(?:-[a-z0-9]+)*', entry.parent.name) or len(entry.parent.name) > 64:
                raise ValueError('Name must match its Android kebab-case directory, at most 64 characters')
            description = metadata.get('description')
            if not isinstance(description, str) or not description.strip() or len(description) > 1024:
                raise ValueError('Description must be nonempty and at most 1024 characters')
            if not parts[2].strip():
                raise ValueError('Skill body is empty')
        except (OSError, UnicodeError, ValueError, TypeError, yaml.YAMLError) as exc:
            errors.append(f'{label}: {exc}')
    for path in root.rglob('*'):
        if path.is_symlink():
            errors.append(f'{path.relative_to(root)}: symlinks are not portable')
    for file in root.rglob('*.md'):
        if file.is_symlink():
            continue
        try:
            text = file.read_text(encoding='utf-8')
        except (OSError, UnicodeError) as exc:
            errors.append(f'{file.relative_to(root)}: {exc}')
            continue
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            target = link.strip().strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme in {'https', 'http', 'mailto'}:
                continue
            if parsed.scheme or parsed.netloc or target.startswith('/'):
                errors.append(f'{file.relative_to(root)}: nonportable link {target}')
                continue
            if not parsed.path:
                continue
            resolved = (file.parent / unquote(parsed.path)).resolve()
            boundary = file.parent if file.name == 'SKILL.md' else root
            if not resolved.is_relative_to(boundary.resolve()):
                errors.append(f'{file.relative_to(root)}: link escapes package boundary: {target}')
            elif not resolved.exists():
                errors.append(f'{file.relative_to(root)}: missing link: {target}')
    try:
        readme = (root / 'README.md').read_text(encoding='utf-8')
        catalog = re.findall(r'^- \[`(android-[^`]+)`\]\(skills/([^/]+)/SKILL\.md\)$', readme, re.MULTILINE)
        listed = [name for name, directory in catalog]
        if any(name != directory for name, directory in catalog) or len(listed) != len(set(listed)) or set(listed) != names:
            errors.append('README catalog must link to each skill exactly once with its matching directory')
    except (OSError, UnicodeError) as exc:
        errors.append(f'README catalog: {exc}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    errors = validate(args.root)
    for error in errors:
        print(f'ERROR: {error}')
    if not errors:
        print(f'Validated {len(list((args.root / "skills").glob("*/SKILL.md")))} Android starter skills.')
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
