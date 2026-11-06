from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import os

app = FastAPI(
    title="Video AI Gratis API",
    version="0.1.0"
)

class GenerateRequest(BaseModel):
    prompt: str = Field(min_length=3)
    negative_prompt: str = ""
    duration_seconds: int = Field(default=30, ge=1, le=30)
    aspect_ratio: str = "9:16"
    image_uri: str = ""

@app.get("/")
def health():
    return {
        "status": "online",
        "app": "Video AI Gratis",
        "generator_configured": bool(
            os.getenv("VIDEO_GENERATOR_URL")
        )
    }

@app.post("/generate")
def generate(req: GenerateRequest):
    raise HTTPException(
        status_code=503,
        detail="Mesin AI video belum dihubungkan."
    )
