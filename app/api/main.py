from fastapi import FastAPI
from pydantic import BaseModel

from app.graph.graph import app as graph_app

api = FastAPI(
    title="SampleSize AI",
    version="1.0.0"
)


class AnalyzeRequest(BaseModel):
    text: str


@api.get("/")
def health():

    return {
        "status": "ok",
        "service": "SampleSize AI"
    }


@api.post("/analyze")
def analyze(request: AnalyzeRequest):

    input_state = {
        "text": request.text
    }

    result = graph_app.invoke(input_state)

    return {
        "success": True,
        "report": result.get("final_report")
    }