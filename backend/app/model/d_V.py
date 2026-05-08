class d_V :
    """Describes the dynamics of HIV virions"""

    def __init__(self, p, c, phi) :
        self.p = p
        self.c = c
        self.phi = phi

    def d_t(self, I, V, C, epsilon_prod) :
        return (1 - epsilon_prod) * self.p * I - self.c * V - self.phi * C * V