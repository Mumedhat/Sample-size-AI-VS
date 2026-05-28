from typing import TypedDict, Optional, Dict, Any, List


class GraphState(TypedDict):
    text: str

    qwen_extraction: Optional[Dict[str, Any]]
    llama_extraction: Optional[Dict[str, Any]]
    deepseek_extraction: Optional[Dict[str, Any]]

    study_type: Optional[str]
    population: Optional[str]
    intervention: Optional[str]

    statistical_test: Optional[str]
    effect_size: Optional[float]
    sample_size: Optional[int]

    bias_risk: Optional[str]
    validity_score: Optional[float]
    validation_issues: Optional[List[str]]

    consensus_confidence: Optional[float]

    final_report: Optional[Dict[str, Any]]