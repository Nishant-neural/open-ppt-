
from fastapi import FastAPI
from pydantic import BaseModel
from pipeline.pipelineGen import generate_presentation

app = FastAPI()


class PromptRequest(BaseModel):
    prompt: str


@app.post("/generate")
def generate(req: PromptRequest):
    result = generate_presentation(req.prompt)
    return result
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)