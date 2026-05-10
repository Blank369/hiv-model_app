from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..core import run_simulation

app = FastAPI(title="HIV Model API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/check")
async def check():
    return {"status": "ok"}

@app.post("/simulate")
async def simulate(request: dict):
    return run_simulation(request)