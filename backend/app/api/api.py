from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from fastapi import Request

from ..core import run_simulation
from ..schemas.requests import SimulationRequest
from ..utils import download_result

app = FastAPI(title="HIV Model API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:5175",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
        "http://127.0.0.1:5175",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/check")
async def check():
    return {"status": "ok"}

@app.post("/simulate")
async def simulate(request: SimulationRequest):
    return run_simulation(request.model_dump())

@app.get("/download-result")
async def download_results():
    return download_result()