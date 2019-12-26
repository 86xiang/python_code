import math


class Equation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getDeta(self):
        return self.b * self.b - 4 * self.a * self.c

    def getRoot1(self):
        if self.getDeta() < 0:
            return 0
        else:
            return (-self.b + math.sqrt(self.getDeta())) / (2 * self.a)

    def getRoot2(self):
        if self.getDeta() < 0:
            return 0
        else:
            return (-self.b - math.sqrt(self.getDeta())) / (2 * self.a)


e1 = Equation(1, 4, 5)
print(e1.getRoot1(), e1.getRoot2())
