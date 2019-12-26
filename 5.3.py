words = input("请输入若干单词，用英文逗号分割：")
word_list = words.split(",")
aset = set()
for i in word_list:
    aset.add(i)
word3 = list(aset)
word3.sort()
print(word3)
