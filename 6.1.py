def isodd(x):
    if int(x) != x:
        print("x不是整数，程序退出")
        return
    elif x // 2 != x / 2:
        return True
    else:
        return False


print(isodd(3))
print(isodd(3.2))
print(isodd(32))
