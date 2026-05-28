from app.llm.ollama_client import OllamaClient

llm = OllamaClient()

print(llm.generate("Say hello in one word"))