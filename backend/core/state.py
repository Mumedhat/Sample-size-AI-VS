from typing import TypedDict, Optional

class GraphState(TypedDict):
    text: str
    study_type: Optional[str]
    effect_size: Optional[float]
    sample_size: Optional[int]
    bias_risk: Optional[str]
    final_output: Optional[dict]