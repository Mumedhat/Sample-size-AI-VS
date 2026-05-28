from typing import TypedDict, Optional, Dict, Any


class GraphState(TypedDict):

    # input
    text: str
    api_key: Optional[str]

    # extractors
    qwen_extraction: Optional[Dict[str, Any]]
    llama_extraction: Optional[Dict[str, Any]]
    deepseek_extraction: Optional[Dict[str, Any]]

    # merged outputs
    study_type: Optional[str]
    population: Optional[str]
    intervention: Optional[str]

    # statistics
    statistical_test: Optional[str]
    effect_size: Optional[float]
    sample_size: Optional[int]

    # reasoning
    consensus_confidence: Optional[float]

    # final output
    final_report: Optional[Dict[str, Any]]