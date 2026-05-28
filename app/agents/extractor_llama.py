from app.llm.ollama_client import OllamaClient
from app.core.json_parser import extract_json
from app.schema.extraction import ExtractionSchema
from app.core.confidence import compute_extraction_confidence
from app.core.normalizer import (
    normalize_study_type,
    normalize_population,
    normalize_intervention
)

llm = OllamaClient(model="llama3.1:8b")


def extractor_llama_node(state):

    text = state.get("text", "")

    prompt = f"""
You are a biomedical study extractor.

Return ONLY valid JSON.

Allowed study types:
- RCT
- cohort
- case-control
- cross-sectional
- unclear

JSON format:

{{
  "study_type": "RCT",
  "population": "string or null",
  "intervention": "string or null"
}}

TEXT:
{text}
"""

    raw = llm.generate(prompt)

    data = extract_json(raw) or {}

    try:

        validated = ExtractionSchema(**data)

        result = validated.model_dump()

    except Exception:

        result = {
            "study_type": "unclear",
            "population": None,
            "intervention": None
        }

    result["study_type"] = normalize_study_type(
        result.get("study_type")
    )

    result["population"] = normalize_population(
        result.get("population")
    )

    result["intervention"] = normalize_intervention(
        result.get("intervention")
    )

    result["confidence"] = compute_extraction_confidence(result)

    return {
        "llama_extraction": result
    }