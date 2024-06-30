import unittest
from copy_my_writing.style_analyzer import StyleAnalyzer


class TestStyleAnalyzer(unittest.TestCase):
    def setUp(self):
        self.style_analyzer = StyleAnalyzer("data/writing_samples.json")

    def test_analyze_word_choice(self):
        expected_word_choice = "Use vivid and descriptive language. Prefer concrete nouns over abstract concepts."
        actual_word_choice = self.style_analyzer.analyze_word_choice()
        self.assertEqual(actual_word_choice, expected_word_choice)

    def test_analyze_sentence_structure(self):
        expected_sentence_structure = "Vary sentence length. Use both short, punchy sentences and longer, flowing ones."
        actual_sentence_structure = self.style_analyzer.analyze_sentence_structure()
        self.assertEqual(actual_sentence_structure, expected_sentence_structure)

    def test_analyze_tone(self):
        expected_tone = (
            "Maintain a reflective and introspective tone. Be personal and authentic."
        )
        actual_tone = self.style_analyzer.analyze_tone()
        self.assertEqual(actual_tone, expected_tone)


if __name__ == "__main__":
    unittest.main()
