def gcd(m, n):
    if m < n:
        m, n = n, m
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
    return n


def lcm(m, n):
    t = m * n
    return int(t / gcd(m, n))


m = eval(input("请输入正整数m:"))
n = eval(input("请输入正整数n:"))
print("最大公约数是", gcd(m, n))
print("最小公倍数是", lcm(m, n))
