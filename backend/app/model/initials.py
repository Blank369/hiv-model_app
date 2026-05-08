class Initials:
    """Storing initial parameter values"""

    def __init__(self, in_T, in_L, in_I, in_V, in_C):
        self.in_T = in_T
        self.in_L = in_L
        self.in_I = in_I
        self.in_V = in_V
        self.in_C = in_C


    def getInits(self):
        return [self.in_T, self.in_L, self.in_I, self.in_V, self.in_C]