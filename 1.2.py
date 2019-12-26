lst = ['hi', "program", 'school', 'for', '''chinese''']
lst1 = []
for item in lst:
    lst1.append(len(item))
p = max(lst1)
for item in lst:
    if len(item) == p:
        print(item, end=" ")
