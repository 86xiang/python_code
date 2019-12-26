# 平均数
def mean(numlist):
    s = 0.0
    for num in numlist:
        s = s + num
    return s / len(numlist)


##标准差=sqrt(((x1-x)^2 +(x2-x)^2 +......(xn-x)^2)/n)
def dev(numlist, mean):
    sdev = 0.0
    for num in numlist:
        sdev = sdev + (num - mean) ** 2
    return (sdev / (len(numlist) - 1)) ** 0.5


def median(numlist):
    numlist.sort()
    half = len(numlist) // 2
    return (numlist[half] + numlist[~half]) / 2


# 函数调用
ls1 = [1, 3, -6, 5, 8]
ls2 = [3.2, 9, -32, 56, 0, 1]

v1 = max(ls2)
v2 = mean(ls2)
v3 = dev(ls2, v2)
v4 = median(ls2)
print("最大值:{:.2f}，平均值:{:.2f}，标准差:{:.2f}，中位数:{:.2f}".format(v1, v2, v3, v4))
