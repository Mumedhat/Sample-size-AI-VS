import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from services.multi_agent import run_single_agent
from validators.schemas import StudyDesignSchema

app = FastAPI()

allowed_origins = os.getenv("CORS_ALLOWED_ORIGINS", "http://localhost:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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