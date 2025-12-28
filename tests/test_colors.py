import unittest
import sys
from run_system import Colors

class TestColors(unittest.TestCase):
    def test_colors_exist(self):
        self.assertTrue(hasattr(Colors, 'HEADER'))
        self.assertTrue(hasattr(Colors, 'BLUE'))
        self.assertTrue(hasattr(Colors, 'ENDC'))

if __name__ == '__main__':
    unittest.main()
