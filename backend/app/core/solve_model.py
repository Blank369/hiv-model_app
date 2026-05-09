import numpy as np
from scipy.integrate import odeint

from .system_odes import system_odes
from ..utils.helpers import write_table

def solve_model(initials, time_params, d_t, d_l, d_i, d_v, d_c, epsilon):
    t = np.linspace(0.0, time_params.dpi_max, int(time_params.dpi_max / time_params.tau))
    result = odeint(
        system_odes,
        initials.getInits(),
        t,
        args=(d_t, d_l, d_i, d_v, d_c, epsilon)
    )
    return t, result
