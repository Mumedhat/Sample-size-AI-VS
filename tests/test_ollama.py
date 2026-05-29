import os
import unittest
from unittest.mock import patch, MagicMock
from app.llm.ollama_client import OllamaClient

class TestOllamaClient(unittest.TestCase):
    @patch.dict(os.environ, clear=True)
    def test_default_url(self):
        # Test that without environment variable, it defaults to localhost
        client = OllamaClient()
        self.assertEqual(client.url, "http://localhost:11434/api/generate")

    @patch.dict(os.environ, {"OLLAMA_URL": "http://custom-ollama:11434/api/generate"}, clear=True)
    def test_custom_url_from_env(self):
        # Test that with environment variable, it uses the provided URL
        client = OllamaClient()
        self.assertEqual(client.url, "http://custom-ollama:11434/api/generate")

    @patch('app.llm.ollama_client.requests.post')
    def test_generate_sends_correct_payload(self, mock_post):
        # Mock the requests.post response
        mock_response = MagicMock()
        mock_response.json.return_value = {"response": "hello"}
        mock_post.return_value = mock_response

        client = OllamaClient(model="test-model")
        result = client.generate("Say hello")

        # Verify the result
        self.assertEqual(result, "hello")

        # Verify requests.post was called with correct arguments
        mock_post.assert_called_once_with(
            client.url,
            json={
                "model": "test-model",
                "prompt": "Say hello",
                "stream": False
            }
        )

if __name__ == '__main__':
    unittest.main()