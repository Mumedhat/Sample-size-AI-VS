from fastapi import FastAPI
from pydantic import BaseModel

from services.multi_agent import run_single_agent
from validators.schemas import StudyDesignSchema

app = FastAPI()


class InputText(BaseModel):
    text: str


@app.get("/")
def root():
    return {"status": "running"}


@app.post("/analyze")
def analyze(input: InputText):

    raw_result = run_single_agent(input.text)

    if not raw_result:
        return {"error": "Invalid AI output"}

    try:
        validated = StudyDesignSchema(**raw_result)
        return validated
    except Exception as e:
        return {"error": str(e), "raw": raw_result}