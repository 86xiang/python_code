s = "abc123^&**KJFDFDLKy"
s2 = ""
for c in s:
    if c.islower():
        c = (ord(c) - ord('a') + 3) % 26 + ord('a')
        # print(chr(c),end="")
    elif c.isupper():
        c = (ord(c) - ord('A') + 3) % 26 + ord('A')
        # print(chr(c),end="")
    else:
        c = ord(c)
    s2 += chr(c)
print(s2)
