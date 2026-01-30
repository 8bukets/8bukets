
import timeit
import re
import unittest

class TestCleanTextOptimization(unittest.TestCase):
    def original_clean_text(self, text):
        if not text:
            return ""
        text = text.replace('\xa0', ' ')
        return re.sub(r'\s+', ' ', text).strip()

    def optimized_clean_text(self, text):
        if not text:
            return ""
        return " ".join(text.split())

    def test_correctness(self):
        test_cases = [
            ("Hello World", "Hello World"),
            ("Hello   World", "Hello World"),
            ("  Hello World  ", "Hello World"),
            ("Hello\xa0World", "Hello World"),
            ("  Hello   \xa0   World  ", "Hello World"),
            ("", ""),
            (None, ""),
            ("   ", ""),
            ("\xa0\xa0", ""),
            ("Multiple\nLines\tHere", "Multiple Lines Here")
        ]

        for input_text, expected in test_cases:
            with self.subTest(input_text=input_text):
                # Test original behavior
                original = self.original_clean_text(input_text)
                self.assertEqual(original, expected, f"Original failed for '{input_text}'")

                # Test optimized behavior
                optimized = self.optimized_clean_text(input_text)
                self.assertEqual(optimized, expected, f"Optimized failed for '{input_text}'")

                # Verify they match
                self.assertEqual(original, optimized)

    def test_benchmark(self):
        text = "  This   is  a   text \xa0 with   irregular   whitespace.  " * 1000
        loops = 10000

        t_orig = timeit.timeit(lambda: self.original_clean_text(text), number=loops)
        t_opt = timeit.timeit(lambda: self.optimized_clean_text(text), number=loops)

        print(f"\nBenchmark (loops={loops}):")
        print(f"Original (Regex): {t_orig:.4f}s")
        print(f"Optimized (Split): {t_opt:.4f}s")
        print(f"Speedup: {t_orig / t_opt:.2f}x")

        self.assertLess(t_opt, t_orig, "Optimization should be faster")

if __name__ == '__main__':
    unittest.main()
