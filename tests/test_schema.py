from validators.schemas import StudyDesignSchema

data = {
    "study_type": "RCT",
    "confidence": 0.9
}

validated = StudyDesignSchema(**data)

print(validated)