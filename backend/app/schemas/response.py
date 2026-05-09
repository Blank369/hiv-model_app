from pydantic import BaseModel
from typing import List, Optional

class SimulationResponse(BaseModel):
    t: List[float]
    T: List[float]
    L: List[float]
    I: List[float]
    V: List[float]
    C: List[float]
    eps_inf: Optional[List[float]] = None
    eps_prod: Optional[List[float]] = None