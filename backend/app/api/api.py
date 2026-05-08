from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
async def simulate():
    return {
        "t": list(range(0, 500, 5)),
        "T": [1000 - i * 0.5 for i in range(100)],
        "L": [0] * 100,
        "I": [0.1] * 100,
        "V": [100 * (1 - i/200) for i in range(100)],
        "C": [50 + i * 0.1 for i in range(100)]
    }