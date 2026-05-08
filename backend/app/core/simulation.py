import numpy as np
from scipy.integrate import odeint

from .system import system_odes
from ..utils.helpers import write_table

def calculate(initials, params, d_t, d_l, d_i, d_v, d_c):
    t = np.linspace(
        0.0,
        params.dpi_max,
        int(params.dpi_max / params.tau)
    )

    result = odeint(
        system_odes,
        initials.getInits(),
        t,
        args=(params, d_t, d_l, d_i, d_v, d_c)
    )

    write_table("result", result, t)

    return t, result