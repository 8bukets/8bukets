import unittest
import sys
from unittest.mock import MagicMock, patch
import schedule
import scheduler

class TestScheduler(unittest.TestCase):

    def setUp(self):
        schedule.clear()

    @patch('scheduler.subprocess.run')
    def test_job_execution(self, mock_run):
        """Test that the job function runs the system script."""
        # Setup mock to return success
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = "Success"
        mock_run.return_value = mock_result

        scheduler.job()

        mock_run.assert_called_once_with([sys.executable, "run_system.py"], capture_output=True, text=True)

    def test_scheduling_interval(self):
        """Test that the job is scheduled every 2 weeks."""
        # We can't easily wait 2 weeks, but we can check the jobs list
        schedule.every(2).weeks.do(scheduler.job)

        jobs = schedule.get_jobs()
        self.assertEqual(len(jobs), 1)
        self.assertEqual(jobs[0].interval, 2)
        self.assertEqual(jobs[0].unit, 'weeks')

if __name__ == '__main__':
    unittest.main()
