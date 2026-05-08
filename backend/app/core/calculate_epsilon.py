from math import exp, pi, sin
from ..model.therapy_modes import TherapyModes

def calculate_epsilon(e0, mode, gamma, t):
    if mode is TherapyModes.THERAPY:
        return e0 if t > gamma else 0.0

    if mode is TherapyModes.INTERRUPTION:
        frequency = 2 * pi / gamma
        return e0 * (sin(frequency * t) + 1) / 2

    if mode is TherapyModes.RESISTANCE:
        return e0 * exp(-gamma * t)

    return 0.0