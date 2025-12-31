import unittest
from unittest.mock import patch
from datetime import datetime
import run_system  # This imports the module where should_run_report is defined

class TestScheduling(unittest.TestCase):

    @patch('run_system.datetime')
    def test_should_run_report_true(self, mock_datetime):
        # Monday of an even week
        # 2024-01-08 is a Monday. Week 2.
        mock_datetime.now.return_value = datetime(2024, 1, 8, 10, 0, 0)
        # Mocking isocalendar is tricky because it's a method on date.
        # But run_system calls datetime.now().isocalendar()
        # So return value of now() needs to support isocalendar()
        # The real datetime object supports it.

        self.assertTrue(run_system.should_run_report())

    @patch('run_system.datetime')
    def test_should_run_report_wrong_day(self, mock_datetime):
        # Tuesday of an even week
        # 2024-01-09 is a Tuesday. Week 2.
        mock_datetime.now.return_value = datetime(2024, 1, 9, 10, 0, 0)
        self.assertFalse(run_system.should_run_report())

    @patch('run_system.datetime')
    def test_should_run_report_wrong_week(self, mock_datetime):
        # Monday of an odd week
        # 2024-01-01 is a Monday. Week 1.
        mock_datetime.now.return_value = datetime(2024, 1, 1, 10, 0, 0)
        self.assertFalse(run_system.should_run_report())

    def test_should_run_report_force(self):
        self.assertTrue(run_system.should_run_report(force=True))

if __name__ == '__main__':
    unittest.main()
