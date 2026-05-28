from pydantic import BaseModel
from typing import Optional


class StudyDesignSchema(BaseModel):
    study_type: str
    confidence: float