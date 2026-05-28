import json
from app.llm.ollama_client import OllamaClient

llm = OllamaClient()

def extractor_node(state):
    text = state["text"]

    prompt = f"""
You are a biomedical research assistant.

Extract study information from the text.

Return ONLY valid JSON:
{{
  "study_type": "RCT | cohort | case-control | observational | unclear",
  "population": "...",
  "intervention": "...",
  "confidence": 0-1
}}

TEXT:
{text}
"""

    response = llm.generate(prompt)

    try:
        data = json.loads(response)
    except:
        data = {
            "study_type": "unclear",
            "population": None,
            "intervention": None,
            "confidence": 0.0
        }

    return {
        **state,
        "study_type": data["study_type"],
        "population": data["population"],
        "intervention": data["intervention"],
        "confidence": data["confidence"]
    }