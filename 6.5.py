def func(s):
    if len(s) < 1:
        return s
    return func(s[1:]) + s[0]


s = "abcde"
result = func(s)
print(result)
