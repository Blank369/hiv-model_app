import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import numpy as np
from fastapi.testclient import TestClient

from app.api import app
from app.core.init_simulation_helpers import (
    create_initial_conditions,
    create_bio_params,
    create_diff_eq_classes,
    create_epsilon,
    create_time_params,
    format_response,
    create_params_dict
)
from app.model.Initials import Initials

client = TestClient(app)

def test_create_initial_conditions():
    initials_dict = {"T": 1000, "L": 0, "I": 0.1, "V": 100, "C": 50}
    obj = create_initial_conditions(initials_dict)
    assert isinstance(obj, Initials)
    assert obj.in_T == 1000
    assert obj.in_L == 0
    assert obj.in_I == 0.1
    assert obj.in_V == 100
    assert obj.in_C == 50


def test_create_bio_params():
    bio = {"lambda_": 10, "r": 0.03, "T_max": 1500, "d_T": 0.01, "beta": 2.4e-5,
           "rho": 0.1, "a": 0.01, "delta_L": 0.001, "delta_I": 0.7, "kappa": 0.001}
    virus = {"p": 100, "c": 10, "phi": 0.001}
    immune = {"s_C": 0.1, "alpha": 0.1, "h": 100, "d_C": 0.01, "eta_C": 0.01, "q": 100}
    params = create_bio_params(bio, virus, immune)
    assert params["lambda_"] == 10
    assert params["p"] == 100
    assert params["s_C"] == 0.1


def test_create_epsilon():
    therapy = {
        "mode_inf": "THERAPY", "epsilon0_inf": 0.9, "gamma_inf": 0.01,
        "mode_prod": "THERAPY", "epsilon0_prod": 0.8, "gamma_prod": 0.01
    }
    eps = create_epsilon(therapy)
    assert eps.epsilon0_inf == 0.9
    assert eps.mode_inf == "THERAPY"


def test_create_time_params():
    sim = {"t_max": 500, "num_points": 1000}
    time_params = create_time_params(sim)
    assert time_params.dpi_max == 500
    assert time_params.tau == 0.5


def test_format_response():
    t = np.array([0, 1, 2])
    result = np.array([[1000, 0, 0, 100, 50],
                       [900, 1, 2, 200, 55],
                       [800, 2, 4, 400, 60]])
    simulation = {
        "t": t,
        "result": result,
        "eps_inf": [0, 0.5, 0.9],
        "eps_prod": [0, 0.4, 0.8]
    }
    response = format_response(simulation)
    assert response["t"] == [0, 1, 2]
    assert response["T"] == [1000, 900, 800]
    assert response["eps_inf"] == [0, 0.5, 0.9]


def test_create_params_dict():
    initials = {"T": 1000}
    bio = {"lambda": 10}
    virus = {"p": 100}
    immune = {"s_C": 0.1}
    therapy = {"mode_inf": "WITHOUT"}
    sim = {"t_max": 500}

    params_dict = create_params_dict(initials, bio, virus, immune, therapy, sim)
    assert params_dict["initials"]["T"] == 1000
    assert params_dict["biological"]["lambda"] == 10
