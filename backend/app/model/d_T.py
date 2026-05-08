class d_T :
    """Description of the target cell population (healthy CD4⁺-T lymphocytes)."""

    def __init__(self, lambda_, r, T_max, d_T, beta) :
        self.lambda_ = lambda_
        self.r = r
        self.T_max = T_max
        self.d_T = d_T
        self.beta = beta

    def d_t(self, T, I, L, V, epsilon_inf) :
        return self.lambda_ + self.r * T * (1 - ((T + I + L) / (self.T_max))) - self.d_T * T - (1 - epsilon_inf) * self.beta * V * T