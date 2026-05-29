from pydantic import BaseModel


class StudyDesignSchema(BaseModel):
    study_type: str
    confidence: float