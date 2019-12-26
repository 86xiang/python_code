import math


class EquationException(Exception):
    def __init__(self, eid, message):  # 异常描述
        self.eid = eid
        self.message = message


class ExceptionDemo:  # 业务逻辑
    def computing(self, a, b, c):
        print("called computing()");
        deta = b * b - 4 * a * c
        if deta < 0:
            raise EquationException(101, "deta值小于零")
        else:
            x1 = (-b + math.sqrt(deta)) / (2 * a)
            x2 = (-b - math.sqrt(deta)) / (2 * a)
            print("一元二次方程的根是{}，{}".format(x1, x2))
            print("normal exit")


myobject = ExceptionDemo()  # 功能测试
try:
    myobject.computing(4, 4, -2)
    myobject.computing(2, 3, 2)
except EquationException as e:
    print("Exception caught,id:{},message:{}".format(e.eid, e.message))
