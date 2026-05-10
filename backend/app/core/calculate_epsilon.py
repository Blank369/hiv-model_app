from math import exp, pi, sin

def calculate_epsilon(e0, mode, gamma, t):
    if mode == 'THERAPY':
        return e0 if t > gamma else 0.0
    elif mode == 'INTERRUPTION':
        frequency = 2 * pi / gamma
        return e0 * (sin(frequency * t) + 1) / 2
    elif mode == 'RESISTANCE':
        return e0 * exp(-gamma * t)
    else:
        return 0.0