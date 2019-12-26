class Movement:
    acceleration = 9.8

    def __init__(self, t):
        self.t = t

    def getSpeed(self):
        return Movement.acceleration * self.t

    def getDistance(self):
        return Movement.acceleration * self.t * self.t / 2


m1 = Movement(3)
print("{:.1f}秒后，速度是{:.2f}，位移是{:.2f}".format(m1.t, m1.getSpeed(), m1.getDistance()))
