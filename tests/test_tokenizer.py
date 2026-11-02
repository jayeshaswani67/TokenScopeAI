
import unittest

from src.tokenizer import count_tokens, analyze_text


class TestTokenizer(unittest.TestCase):

    def test_empty_text(self):
        result = count_tokens("")

        self.assertEqual(result, 0)

    def test_normal_text(self):
        result = count_tokens(
            "Hello world",
            "gpt-4o"
        )

        self.assertGreater(result, 0)

    def test_repeated_text(self):
        text = "Artificial intelligence " * 10

        result = count_tokens(text)

        self.assertGreater(result, 10)

    def test_token_count_consistency(self):
        text = "Explain machine learning."

        first_count = count_tokens(text)

        second_count = count_tokens(text)

        self.assertEqual(
            first_count,
            second_count
        )

    def test_unicode_text(self):
        text = "Hello नमस्ते 世界 🚀"

        result = count_tokens(text)

        self.assertGreater(result, 0)

    def test_unknown_model_fallback(self):
        result = count_tokens(
            "Testing fallback tokenizer",
            "unknown-model"
        )

        self.assertGreater(result, 0)

    def test_analyze_text(self):
        text = "Hello world"

        result = analyze_text(text)

        self.assertEqual(
            result["characters"],
            len(text)
        )

        self.assertEqual(
            result["words"],
            2
        )

        self.assertGreater(
            result["tokens"],
            0
        )


if __name__ == "__main__":

    unittest.main()
