from .calculate_epsilon import calculate_epsilon

def system_odes(inits, t, params, d_t, d_l, d_i, d_v, d_c):
    T, L, I, V, C = inits

    epsilon_inf = calculate_epsilon(
        params.epsilon0_inf,
        params.mode_inf,
        params.gamma_inf,
        t
    )

    epsilon_prod = calculate_epsilon(
        params.epsilon0_prod,
        params.mode_prod,
        params.gamma_prod,
        t
    )

    dT_dt = d_t.d_t(T, I, L, V, epsilon_inf)
    dL_dt = d_l.d_t(T, L, V, epsilon_inf)
    dI_dt = d_i.d_t(T, L, V, I, C, epsilon_inf)
    dV_dt = d_v.d_t(I, V, C, epsilon_prod)
    dC_dt = d_c.d_t(T, I, C)

    return [
        dT_dt,
        dL_dt,
        dI_dt,
        dV_dt,
        dC_dt
    ]