sum = 0
for i in range(1, 100):
    if i % 2 == 1:
        sum += i**2
    else:
        sum -= i**2
print("1²-2²+3²-4²+…+97²-98²+99²=" + str(sum))
