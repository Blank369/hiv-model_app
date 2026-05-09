from pydantic import BaseModel
from typing import Dict, Any

class SimulationRequest(BaseModel):
    initials: Dict[str, float]
    biological: Dict[str, float]
    virus: Dict[str, float]
    immune: Dict[str, float]
    therapy: Dict[str, Any]
    sim: Dict[str, Any]