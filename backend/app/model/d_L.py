class d_L :
    """Description of the number of latently infected cells"""

    def __init__(self, rho, beta, a, delta_L) :
        self.rho = rho
        self.beta = beta
        self.a = a
        self.delta_L = delta_L

    def d_t(self, T, L, V, epsilon_inf) :
        return self.rho * (1 - epsilon_inf) * self.beta * V * T - self.a * L - self.delta_L * L