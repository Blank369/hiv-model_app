from pydantic import BaseModel, Field
from typing import Literal


class InitialsSchema(BaseModel):
    T: float = Field(ge=0)
    L: float = Field(ge=0)
    I: float = Field(ge=0)
    V: float = Field(ge=0)
    C: float = Field(ge=0)


class BioSchema(BaseModel):
    lambda_: float = Field(alias="lambda", ge=0)

    r: float = Field(ge=0)
    T_max: float = Field(ge=0)
    d_T: float = Field(ge=0)

    beta: float = Field(ge=0)
    rho: float = Field(ge=0)
    a: float = Field(ge=0)

    delta_L: float = Field(ge=0)
    delta_I: float = Field(ge=0)

    kappa: float = Field(ge=0)


class VirusSchema(BaseModel):
    p: float = Field(ge=0)
    c: float = Field(ge=0)
    phi: float = Field(ge=0)


class ImmuneSchema(BaseModel):
    s_C: float = Field(ge=0)
    alpha: float = Field(ge=0)
    h: float = Field(ge=0)

    d_C: float = Field(ge=0)
    eta_C: float = Field(ge=0)
    q: float = Field(ge=0)


class TherapySchema(BaseModel):
    mode_inf: Literal[
        "WITHOUT",
        "THERAPY",
        "INTERRUPTION",
        "RESISTANCE"
    ]

    mode_prod: Literal[
        "WITHOUT",
        "THERAPY",
        "INTERRUPTION",
        "RESISTANCE"
    ]

    epsilon0_inf: float = Field(ge=0, le=1)
    gamma_inf: float = Field(ge=0)

    epsilon0_prod: float = Field(ge=0, le=1)
    gamma_prod: float = Field(ge=0)


class SimulationSchema(BaseModel):
    t_max: float = Field(gt=0)
    num_points: int = Field(gt=0)


class SimulationRequest(BaseModel):
    initials: InitialsSchema
    biological: BioSchema
    virus: VirusSchema
    immune: ImmuneSchema
    therapy: TherapySchema
    sim: SimulationSchema

