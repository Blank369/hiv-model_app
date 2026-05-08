class d_I :
    """Description of the number of productively infected cells"""

    def __init__(self, rho, beta, a, delta_I, kappa) :
        self.rho = rho
        self.beta = beta
        self.a = a
        self.delta_I = delta_I
        self.kappa = kappa

    def d_t(self, T, L, V, I, C, epsilon_inf) :
        return (1 - self.rho) * (1 - epsilon_inf) * self.beta * V * T + self.a * L - self.delta_I * I - self.kappa * C * I