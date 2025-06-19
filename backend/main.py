from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import logging

from chart_builder import build_chart_config, export_chart
from llama_insight import generate_insight
from data_provider import get_user_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI"}

@app.post("/chat")
async def chat_handler(request: Request):
    try:
        body = await request.json()
        intent = body.get("intent")

        if not intent:
            return JSONResponse(content={"error": "Missing intent."}, status_code=400)

        data = get_user_data(intent)
        if not data:
            return JSONResponse(content={"error": "Invalid intent."}, status_code=404)

        chart_config = build_chart_config(intent, data)
        chart_path = export_chart(chart_config, intent)
        insight = generate_insight(intent, data)

        return {
            "chart_url": f"/static/{chart_path}",
            "insight": insight
        }

    except Exception as e:
        logger.exception("Error in /chat")
        return JSONResponse(
            content={"error": f"Internal Server Error: {str(e)}"},
            status_code=500
        )
