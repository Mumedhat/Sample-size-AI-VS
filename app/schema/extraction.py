from pydantic import BaseModel
from typing import Optional


class ExtractionSchema(BaseModel):

    study_type: str = "unclear"

    population: Optional[str] = None

    intervention: Optional[str] = None