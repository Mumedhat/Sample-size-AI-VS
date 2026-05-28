from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import fitz  # PyMuPDF
import docx
import io
import os

from app.graph.graph import app as graph_app

api = FastAPI(
    title="SampleSize AI",
    version="1.0.0"
)


class AnalyzeRequest(BaseModel):
    text: str


# Serve static files for the frontend SaaS UI
static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    api.mount("/static", StaticFiles(directory=static_dir), name="static")

@api.get("/", response_class=HTMLResponse)
def root():
    index_path = os.path.join(static_dir, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>SampleSize AI API</h1><p>Frontend not found.</p>"

@api.get("/health")
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

@api.post("/analyze_file")
async def analyze_file(file: UploadFile = File(...)):
    filename = file.filename.lower()
    text = ""

    try:
        content = await file.read()

        if filename.endswith(".pdf"):
            pdf_document = fitz.open(stream=content, filetype="pdf")
            for page in pdf_document:
                text += page.get_text()
            pdf_document.close()
        elif filename.endswith(".docx"):
            doc = docx.Document(io.BytesIO(content))
            text = "\n".join([para.text for para in doc.paragraphs])
        else:
            raise HTTPException(status_code=400, detail="Only PDF and DOCX files are supported.")

        if not text.strip():
            raise HTTPException(status_code=400, detail="Could not extract text from the file or file is empty.")

        input_state = {
            "text": text
        }

        result = graph_app.invoke(input_state)

        return {
            "success": True,
            "report": result.get("final_report")
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))