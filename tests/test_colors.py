import unittest
from scraper import Colors

class TestColors(unittest.TestCase):
    def test_strip_colors(self):
        text = "\033[95mHello\033[0m"
        self.assertEqual(Colors.strip(text), "Hello")

    def test_strip_no_colors(self):
        text = "Hello World"
        self.assertEqual(Colors.strip(text), "Hello World")
