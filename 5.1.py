import random

letters1 = "ABCDEFGHIJKLMN"
letters2 = "opqrstuvwxyz"
letters3 = "0123456789"
letters = letters1 + letters2 + letters3
code = ""
for i in range(4):
    code += random.choice(letters)
print("产生的验证码是：{}".format(code))
