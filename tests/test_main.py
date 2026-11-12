import io
import unittest
from contextlib import redirect_stdout
from types import SimpleNamespace
from unittest.mock import patch

import main


class ApiKeyTests(unittest.TestCase):
    @patch("main.load_dotenv")
    @patch("main.os.getenv", return_value="test-api-key")
    def test_get_api_key(self, mock_getenv, mock_load_dotenv):
        self.assertEqual(main.get_api_key(), "test-api-key")
        mock_load_dotenv.assert_called_once_with()
        mock_getenv.assert_called_once_with("GROQ_API_KEY")

    @patch("main.load_dotenv")
    def test_missing_api_key_raises(self, _mock_load_dotenv):
        for value in (None, ""):
            with self.subTest(value=value):
                with patch("main.os.getenv", return_value=value):
                    with self.assertRaisesRegex(RuntimeError, "GROQ_API_KEY"):
                        main.get_api_key()


class MainTests(unittest.TestCase):
    @patch("main.Groq")
    @patch("main.get_api_key", return_value="test-api-key")
    def test_main_calls_groq_and_prints_response(self, _mock_key, mock_groq):
        mock_create = mock_groq.return_value.chat.completions.create
        mock_create.return_value = SimpleNamespace(
            choices=[
                SimpleNamespace(
                    message=SimpleNamespace(content="An API connects software.")
                )
            ]
        )

        output = io.StringIO()
        with redirect_stdout(output):
            main.main()

        mock_groq.assert_called_once_with(api_key="test-api-key")
        mock_create.assert_called_once_with(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": "Explain what an API is in 2 sentences."}],
        )
        self.assertEqual(output.getvalue(), "An API connects software.\n")


if __name__ == "__main__":
    unittest.main()
