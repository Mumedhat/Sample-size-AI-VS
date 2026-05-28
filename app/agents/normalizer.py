def normalize_extraction(extraction: dict):
    if not extraction:
        return {}

    return {
        "study_type": (extraction.get("study_type") or "unclear").lower().strip(),
        "population": extraction.get("population") or "unknown",
        "intervention": extraction.get("intervention") or "unknown",
        "confidence": float(extraction.get("confidence") or 0.0)
    }


# =========================
# LANGGRAPH NODE WRAPPER
# =========================

def normalizer_node(state: dict):
    """
    Normalizes all extractor outputs before consensus.
    """

    state["qwen_extraction"] = normalize_extraction(state.get("qwen_extraction"))
    state["llama_extraction"] = normalize_extraction(state.get("llama_extraction"))
    state["deepseek_extraction"] = normalize_extraction(state.get("deepseek_extraction"))

    return state