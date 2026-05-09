from .calculate_epsilon import calculate_epsilon

def system_odes(y, t, dT, dL, dI, dV, dC, epsilon):
    T, L, I, V, C = y

    eps_inf = calculate_epsilon(
        epsilon.epsilon0_inf,
        epsilon.mode_inf,
        epsilon.gamma_inf,
        t
    )
    eps_prod = calculate_epsilon(
        epsilon.epsilon0_prod,
        epsilon.mode_prod,
        epsilon.gamma_prod,
        t
    )

    dT_dt = dT.d_t(T, I, L, V, eps_inf)
    dL_dt = dL.d_t(T, L, V, eps_inf)
    dI_dt = dI.d_t(T, L, V, I, C, eps_inf)
    dV_dt = dV.d_t(I, V, C, eps_prod)
    dC_dt = dC.d_t(T, I, C)

    return [dT_dt, dL_dt, dI_dt, dV_dt, dC_dt]