"""
FastAPI app for the COVIS AI Copilot POC.

Endpoints:
- GET  /              → chat UI
- POST /chat          → send a message, get AI response
- POST /lead-summary  → generate lead summary
- GET  /health        → basic health check
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from .llm import get_response, get_lead_summary

app = FastAPI(title="COVIS AI Copilot POC")

# Static files (CSS)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates (HTML)
templates = Jinja2Templates(directory="app/templates")


# ---------- Request models ----------
class ChatRequest(BaseModel):
    message: str


# ---------- Routes ----------
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    """Serve the chat UI."""
    return templates.TemplateResponse(request, "index.html")


@app.post("/chat")
def chat(payload: ChatRequest):
    """Receive a user message, return AI response."""
    if not payload.message or not payload.message.strip():
        return JSONResponse(
            {"reply": "Please say something."},
            status_code=400,
        )

    reply = get_response(payload.message.strip())
    return {"reply": reply}


@app.post("/lead-summary")
def lead_summary():
    """Return a summary of this week's leads and follow-ups."""
    summary = get_lead_summary()
    return {"reply": summary}


@app.get("/health")
def health():
    """Simple health check."""
    return {"status": "ok"}