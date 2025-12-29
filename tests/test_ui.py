
import unittest
from utils.ui import Colors, print_summary_box
import io
import sys

class TestUI(unittest.TestCase):
    def test_strip_ansi(self):
        # Use FAIL which corresponds to red/failure color in our class
        text = f"{Colors.FAIL}Hello{Colors.ENDC}"
        clean = Colors.strip_ansi(text)
        self.assertEqual(clean, "Hello")

    def test_print_summary_box(self):
        # Capture stdout
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        stats = {
            "Time": "1.23s",
            "Status": Colors.style("Success", Colors.GREEN)
        }

        print_summary_box(stats)
        sys.stdout = sys.__stdout__

        output = capturedOutput.getvalue()
        self.assertIn("EXECUTION SUMMARY", output)
        self.assertIn("Time", output)
        self.assertIn("1.23s", output)
        self.assertIn("Success", output)
        # Check if box width is consistent (rough check by looking for border)
        self.assertIn("=====", output)

if __name__ == '__main__':
    unittest.main()
