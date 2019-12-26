try:
    chars = ['a', 'b', 'c', 'd', 'e']
    chars[4] = 1
    print(chars)
    chars[5] = 'xx'
except IndexError:
    print("索引超过范围")
