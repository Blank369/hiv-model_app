class Initials:
    """Storing initial parameter values"""

    def __init__(self, in_T = 1000, in_L = 0.0, in_I = 1, in_V = 10, in_C = 0.0):
        self.in_T = in_T
        self.in_L = in_L
        self.in_I = in_I
        self.in_V = in_V
        self.in_C = in_C


    def getInits(self):
        return [self.in_T, self.in_L, self.in_I, self.in_V, self.in_C]