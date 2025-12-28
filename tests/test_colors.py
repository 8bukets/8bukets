import unittest
from unittest.mock import patch
import sys
import io
from scraper import Colors, WordpressScraperAsync

class TestColors(unittest.TestCase):
    def test_colors_exist(self):
        self.assertTrue(hasattr(Colors, 'HEADER'))
        self.assertTrue(hasattr(Colors, 'BLUE'))
        self.assertTrue(hasattr(Colors, 'ENDC'))

class TestSummaryBox(unittest.TestCase):
    def setUp(self):
        self.scraper = WordpressScraperAsync(
            base_url="https://example.com/",
            output_json="long_filename_that_needs_truncation_to_fit_in_the_box.json",
            output_csv="test.csv",
            output_txt="test.txt"
        )

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_summary_truncation(self, mock_stdout):
        # Force isatty to be True for testing
        with patch('sys.stdout.isatty', return_value=True):
            self.scraper.print_summary(10, 5)
            output = mock_stdout.getvalue()

            # Check for truncation
            self.assertIn("long_filename_that_needs_trunca...", output)
            self.assertIn("Total Posts:", output)
            self.assertIn("10", output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_summary_no_tty(self, mock_stdout):
        # Force isatty to be False
        with patch('sys.stdout.isatty', return_value=False):
            # Ensure FORCE_COLOR is not set
            with patch.dict('os.environ', {}, clear=True):
                self.scraper.print_summary(10, 5)
                output = mock_stdout.getvalue()
                self.assertEqual(output, "")

if __name__ == '__main__':
    unittest.main()
