import numpy as np
from scipy.integrate import odeint

from .calculate_epsilon import calculate_epsilon
from .system_odes import system_odes


def solve_model(initials, time_params, equations, epsilon):
    t = np.linspace(
        0.0,
        time_params.dpi_max,
        int(time_params.dpi_max / time_params.tau)
    )

    result = odeint(
        system_odes,
        initials.getInits(),
        t,
        args=(*equations, epsilon)
    )

    eps_inf = [
        calculate_epsilon(
            epsilon.epsilon0_inf,
            epsilon.mode_inf,
            epsilon.gamma_inf,
            ti
        )
        for ti in t
    ]

    eps_prod = [
        calculate_epsilon(
            epsilon.epsilon0_prod,
            epsilon.mode_prod,
            epsilon.gamma_prod,
            ti
        )
        for ti in t
    ]

    return {
        "t": t,
        "result": result,
        "eps_inf": eps_inf,
        "eps_prod": eps_prod
    }