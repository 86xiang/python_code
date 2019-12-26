class StuGroup:
    total = count = 0

    def setScore(self, score):
        self.score = score

    def getScore(self):
        return self.score

    def __init__(self, score):
        self.setScore(score)
        StuGroup.count += 1
        self.sum()

    def sum(self):
        StuGroup.total += self.getScore()

    @classmethod
    def average(cls):
        return StuGroup.total / StuGroup.count

    @classmethod
    def show(cls):
        print("总分是：{}".format(StuGroup.total))
        print("总分是：{}".format(StuGroup.average()))


s1 = StuGroup(90)
s2 = StuGroup(87)
s3 = StuGroup(93)
StuGroup.show()
