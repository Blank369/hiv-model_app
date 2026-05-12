from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)

def test_check_api():
    response = client.get("/check")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_simulate_api():
    payload = {
        "initials": {"T": 1000, "L": 0, "I": 0, "V": 1000, "C": 500},
        "biological": {"lambda": 10, "r": 0.03, "T_max": 1500, "d_T": 0.01, "beta": 2.4e-5,
                       "rho": 0.1, "a": 0.01, "delta_L": 0.001, "delta_I": 0.7, "kappa": 0.001},
        "virus": {"p": 100, "c": 10, "phi": 0.001},
        "immune": {"s_C": 0.1, "alpha": 0.1, "h": 100, "d_C": 0.01, "eta_C": 0.01, "q": 100},
        "therapy": {"mode_inf": "WITHOUT", "mode_prod": "WITHOUT",
                    "epsilon0_inf": 0, "gamma_inf": 0, "epsilon0_prod": 0, "gamma_prod": 0},
        "sim": {"t_max": 10, "num_points": 100}
    }

    response = client.post("/simulate", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert "t" in data
    assert len(data["t"]) == 100


def test_missing_required_field():
    payload = {
        "initials": {"T": 1000},
        "biological": {},
        "virus": {},
        "immune": {},
        "therapy": {},
        "sim": {}
    }
    response = client.post("/simulate", json=payload)
    assert response.status_code == 422