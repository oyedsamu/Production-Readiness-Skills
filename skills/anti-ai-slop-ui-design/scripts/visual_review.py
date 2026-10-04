#!/usr/bin/env python3
"""Track visual review evidence; never infer aesthetics from files or CSS."""
import argparse
import json
from pathlib import Path

CHECKS = ('context', 'concept', 'three_directions', 'selected_language', 'product_fit',
          'distinctiveness', 'hierarchy', 'coherence', 'usability', 'accessibility',
          'responsiveness', 'density', 'personality', 'restraint', 'copy_content', 'anti_patterns')
WIDTHS = (320, 390, 430, 1280, 1440)
STATES = ('primary', 'navigation', 'loading', 'empty', 'error', 'long_content', 'dense_data')
STATUSES = {'PASS', 'WARN', 'FAIL', 'UNVERIFIED', 'N/A'}


def template():
    def entry(identifier):
        return {'id': identifier, 'status': 'UNVERIFIED', 'evidence': '', 'reason': ''}
    return {'version': 1, 'candidate': '', 'platform': '',
            'checks': [entry(x) for x in CHECKS],
            'renders': [dict(entry(str(x)), screenshot='') for x in WIDTHS],
            'states': [dict(entry(x), screenshot='') for x in STATES],
            'refinement': {'observation': '', 'action_or_rejected_alternatives': '',
                           'before': '', 'after': '', 'reinspection': ''}}


def validate(record, root):
    errors = []
    def require_text(value, label):
        if not isinstance(value, str) or not value.strip():
            errors.append(f'{label}: text required')
    def screenshot(value, label):
        require_text(value, label)
        if isinstance(value, str) and value.strip():
            path = root / value
            if path.suffix.lower() not in {'.png', '.jpg', '.jpeg', '.webp'} or not path.is_file() or path.stat().st_size == 0:
                errors.append(f'{label}: nonempty screenshot file required')
    if not isinstance(record, dict):
        return ['Record must be an object']
    if record.get('version') != 1:
        errors.append('Unsupported record version')
    for field in ('candidate', 'platform'):
        require_text(record.get(field), field)
    for section, required in (('checks', CHECKS), ('renders', tuple(map(str, WIDTHS))), ('states', STATES)):
        entries = record.get(section)
        if not isinstance(entries, list):
            errors.append(f'{section}: list required')
            continue
        seen = set()
        for entry in entries:
            if not isinstance(entry, dict) or not isinstance(entry.get('id'), str):
                errors.append(f'{section}: entry with string id required')
                continue
            identifier = entry['id']
            label = f'{section}.{identifier}'
            if identifier in seen:
                errors.append(f'{label}: duplicate id')
            seen.add(identifier)
            status = entry.get('status')
            if not isinstance(status, str) or status not in STATUSES:
                errors.append(f'{label}: invalid status')
                continue
            if status in {'FAIL', 'UNVERIFIED'}:
                errors.append(f'{label}: {status}')
            if status == 'N/A':
                require_text(entry.get('reason'), label + '.reason')
                if section == 'checks':
                    errors.append(f'{label}: core design checks cannot be N/A')
            else:
                require_text(entry.get('evidence'), label + '.evidence')
                if status == 'WARN':
                    require_text(entry.get('reason'), label + '.impact_and_followup')
                if section in {'renders', 'states'} and status in {'PASS', 'WARN'}:
                    screenshot(entry.get('screenshot'), label + '.screenshot')
        for identifier in set(required) - seen:
            errors.append(f'{section}.{identifier}: missing')
        if section in {'renders', 'states'} and not any(isinstance(e, dict) and e.get('status') in {'PASS', 'WARN'} for e in entries):
            errors.append(f'{section}: at least one actual inspection required')
    refinement = record.get('refinement')
    if not isinstance(refinement, dict):
        errors.append('refinement: object required')
    else:
        for field in ('observation', 'action_or_rejected_alternatives', 'reinspection'):
            require_text(refinement.get(field), 'refinement.' + field)
        for field in ('before', 'after'):
            screenshot(refinement.get(field), 'refinement.' + field)
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('init').add_argument('--output', type=Path, required=True)
    commands.add_parser('check').add_argument('record', type=Path)
    args = parser.parse_args()
    try:
        if args.command == 'init':
            with args.output.open('x') as file:
                json.dump(template(), file, indent=2)
                file.write('\n')
            print(f'Created {args.output}; complete it after actual inspection.')
            return 0
        errors = validate(json.loads(args.record.read_text()), args.record.resolve().parent)
    except (OSError, ValueError) as exc:
        print(f'ERROR: {exc}')
        return 2
    for error in errors:
        print('ERROR: ' + error)
    print('EVIDENCE RECORD INCOMPLETE' if errors else 'EVIDENCE RECORD COMPLETE — visual judgment remains manual')
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
