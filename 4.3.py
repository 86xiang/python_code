s = 0
flag = 1
for i in range(1, 100):
    s = s + i * i * flag
    flag *= -1

print(s)
