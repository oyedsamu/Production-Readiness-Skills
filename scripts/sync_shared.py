#!/usr/bin/env python3
"""Copy canonical review references into independently installable skills."""
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARED = ("review-method.md", "reporting.md", "domain-checks.md")


def sync(root=ROOT, check=False):
    stale = []
    for skill in sorted((root / "skills").glob("*/SKILL.md")):
        for name in SHARED:
            source = root / "templates" / name
            destination = skill.parent / "references" / name
            if not destination.exists() or destination.read_bytes() != source.read_bytes():
                stale.append(str(destination.relative_to(root)))
                if not check:
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    destination.write_bytes(source.read_bytes())
    return stale


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail on drift without writing")
    args = parser.parse_args()
    stale = sync(check=args.check)
    for path in stale:
        print(("STALE " if args.check else "UPDATED ") + path)
    if not stale:
        print("Shared references are synchronized.")
    return int(args.check and bool(stale))


if __name__ == "__main__":
    raise SystemExit(main())
