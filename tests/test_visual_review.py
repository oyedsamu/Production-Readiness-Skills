"""Exercise evidence gate failures, not subjective visual aesthetics."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/anti-ai-slop-ui-design/scripts/visual_review.py'
spec = importlib.util.spec_from_file_location('visual_review', SCRIPT)
review = importlib.util.module_from_spec(spec)
spec.loader.exec_module(review)


class VisualReviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        # An evidence-file fixture; no claim of pixel or aesthetic validation.
        (self.root/'screen.png').write_bytes(b'file-existence fixture')
        self.record = review.template()
        self.record.update(candidate='fixture-version', platform='responsive-web')
        for section in ('checks', 'renders', 'states'):
            for entry in self.record[section]:
                entry.update(status='PASS', evidence='Recorded inspection fixture')
                if section != 'checks':
                    entry['screenshot'] = 'screen.png'
        self.record['refinement'] = dict(observation='Fixture issue', action_or_rejected_alternatives='Fixture action', before='screen.png', after='screen.png', reinspection='Fixture result')

    def test_complete_record(self):
        self.assertEqual(review.validate(self.record, self.root), [])

    def test_unfilled_template_blocks(self):
        self.assertTrue(review.validate(review.template(), self.root))

    def test_missing_screenshot_blocks(self):
        self.record['renders'][0]['screenshot'] = 'absent.png'
        self.assertTrue(review.validate(self.record, self.root))

    def test_missing_check_and_duplicate_block(self):
        self.record['checks'][0] = copy.deepcopy(self.record['checks'][1])
        errors = review.validate(self.record, self.root)
        self.assertTrue(any('duplicate' in x for x in errors))
        self.assertTrue(any('missing' in x for x in errors))

    def test_invalid_structure_does_not_crash(self):
        for value in ([], None, {'checks': 'bad'}, {'version': 1, 'checks': [{'id': 'context', 'status': []}]}):
            self.assertTrue(review.validate(value, self.root))

    def test_fail_and_unverified_block(self):
        for status in ('FAIL', 'UNVERIFIED'):
            self.record['checks'][0]['status'] = status
            self.assertTrue(review.validate(self.record, self.root))

    def test_warn_requires_impact_followup(self):
        self.record['checks'][0]['status'] = 'WARN'
        self.assertTrue(review.validate(self.record, self.root))
        self.record['checks'][0]['reason'] = 'Minor fixture issue; follow up next iteration'
        self.assertEqual(review.validate(self.record, self.root), [])

    def test_na_requires_reason_and_real_inspection(self):
        for entry in self.record['renders']:
            entry.update(status='N/A', reason='Native application; use added device-size entry')
        self.assertTrue(review.validate(self.record, self.root))
        self.record['renders'].append(dict(id='native-phone', status='PASS', evidence='Fixture', screenshot='screen.png'))
        self.assertEqual(review.validate(self.record, self.root), [])

    def test_missing_refinement_blocks(self):
        self.record['refinement']['after'] = ''
        self.assertTrue(review.validate(self.record, self.root))

    def test_cli_init_check_and_no_overwrite(self):
        path = self.root/'review.json'
        def run(*args):
            return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True)
        self.assertEqual(run('init', '--output', str(path)).returncode, 0)
        self.assertEqual(run('init', '--output', str(path)).returncode, 2)
        self.assertEqual(run('check', str(path)).returncode, 1)
        path.write_text(json.dumps(self.record))
        self.assertEqual(run('check', str(path)).returncode, 0)
        path.write_text('{invalid')
        self.assertEqual(run('check', str(path)).returncode, 2)


if __name__ == '__main__':
    unittest.main()
