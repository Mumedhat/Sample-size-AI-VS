from services.ollama_client import ask_ollama
from services.json_parser import safe_json_parse


def run_single_agent(text: str):
    prompt = f"""
You are a medical research assistant.

Extract ONLY the study design.

Return ONLY valid JSON:

{{
  "study_type": "RCT / cohort / case-control / observational",
  "confidence": 0-1
}}

Text:
{text}

RULES:
- Return ONLY JSON
- No explanation
"""

    raw = ask_ollama("qwen2.5:7b", prompt)

    parsed = safe_json_parse(raw)

    return parsed