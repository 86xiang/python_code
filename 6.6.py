def func(sum):
    for i in range(1, 100):
        if i % 2 == 1:
            sum += i ** 2
        else:
            sum -= i ** 2
    print(sum)


sum = 0
func(sum)
