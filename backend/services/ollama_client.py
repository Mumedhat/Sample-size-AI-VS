import requests
import json
import os

class OllamaClient:
    def __init__(self, model="qwen2.5:7b"):
        self.local_model = model
        # Map local ollama models to free Groq endpoints
        self.model_map = {
            "qwen2.5:7b": "gemma2-9b-it",
            "llama3.1:8b": "llama-3.1-8b-instant",
            "deepseek-r1:8b": "mixtral-8x7b-32768"
        }
        self.groq_model = self.model_map.get(model, "llama-3.1-8b-instant")
        self.url = "https://api.groq.com/openai/v1/chat/completions"

    def generate(self, prompt: str, api_key: str = None):
        if not api_key:
            api_key = os.environ.get("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY is not set. Please provide an API key to use the free Groq AI agents.")

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        data = {
            "model": self.groq_model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_completion_tokens": 1024,
            "stream": False
        }

        try:
            response = requests.post(self.url, headers=headers, json=data, timeout=30)
            if response.status_code == 200:
                result = response.json()
                return result["choices"][0]["message"]["content"]
            else:
                raise Exception(f"Groq API Error ({response.status_code}): {response.text}")
        except Exception as e:
            raise Exception(f"Failed to extract info via Groq: {str(e)}")

def ask_ollama(model: str, prompt: str, api_key: str = None):
    client = OllamaClient(model=model)
    return client.generate(prompt, api_key=api_key)