def change(str1):
    t = ""
    for i in range(len(str1)):
        if str1[i].islower():
            t += str1[i].upper()
        elif str1[i].isupper():
            t += str1[i].lower()
        else:
            t += str1[i]
    return t


print(change("iu98kLLD"))
