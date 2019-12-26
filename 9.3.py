import os.path

filename = input("请输入文件的全名:")
if os.path.exists(filename):
    print("该文件存在于当前目录下")
    print("-----下面是文件信息-------")
    print("文件大小是：", os.path.getsize(filename))
    if os.path.isfile(filename):
        print(filename, "是一个文件")
    else:
        print(filename, "是一个目录")
else:
    print("该文件不存在！")
