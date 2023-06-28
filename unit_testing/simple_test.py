import unittest
import case


class TitleCase(unittest.TestCase):
    def test_single_word(self):
        text = "python"
        result = case.title_case(text)
        self.assertEqual(result, "Python")

    def test_multiple_words(self):
        text = "python programming"
        result = case.title_case(text)
        self.assertEqual(result, "Python Programming")


if __name__ == "__main__":
    unittest.main()
