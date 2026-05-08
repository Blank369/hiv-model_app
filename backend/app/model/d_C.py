class d_C:
    """Describes the number of immune effector cells"""

    def __init__(self, s_C, alpha, h, d_C, eta_C, q):
        self.s_C = s_C
        self.alpha = alpha
        self.h = h
        self.d_C = d_C
        self.eta_C = eta_C
        self.q = q

    def d_t(self, T, I, C):
        return self.s_C + ((self.alpha * T * C) / (T * C + self.h)) - self.d_C * C - self.eta_C * C * (I / (I + self.q))
