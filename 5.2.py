stu1 = {"no": 101, "name": "Rose", "address": "Changjianroad", "score": 92}
stu2 = dict(id=201, name="Mike", address="Huangheroad", score=83)
stu3 = dict([('id', 103), ('name', 'Kate'), ('address', 'Xinanroad'), ('pcode', '116033'), ('score', 90)])
lst = [stu1, stu2, stu3]
var = input("请输入要查找学生的姓名：")
result = False
for item in lst:
    if var.strip() in item.values():
        print(item)
        result = True
if not result:
    print("信息不存在")
