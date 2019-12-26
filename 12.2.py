import tkinter
import tkinter.messagebox
import sqlite3

# 创建应用程序窗口
win = tkinter.Tk()
varName = tkinter.StringVar()
varName.set('')
varPwd = tkinter.StringVar()
varPwd.set('')
# 创建标签
labelName = tkinter.Label(text='User Name:', justify=tkinter.RIGHT, width=80)
labelName.place(x=10, y=5, width=80, height=20)
# 创建文本框，同时设置关联的变量
entryName = tkinter.Entry(win, width=80, textvariable=varName)
entryName.place(x=100, y=5, width=80, height=20)
labelPwd = tkinter.Label(win, text='User Pwd:', justify=tkinter.RIGHT, width=80)
labelPwd.place(x=10, y=30, width=80, height=20)
# 创建密码文本框
entryPwd = tkinter.Entry(win, show='*', width=80, textvariable=varPwd)
entryPwd.place(x=100, y=30, width=80, height=20)


# 连接数据库的通用函数
def getConnection():
    dbstring = "d:/sqlite/test.db"
    conn = sqlite3.connect(dbstring)
    return conn
    # print(getConnection()) 测试连接是否成功


def login():  # 登录按钮事件数理函数
    # 获取用户名和密码
    name = entryName.get()
    pwd = entryPwd.get()
    # 获取数据中数据
    dbinfo = getConnection()
    cur = dbinfo.cursor()
    sqlstr = "select * from user where username=? and pwd=?"
    cur.execute(sqlstr, (name, pwd))
    if cur.fetchone() != None:  # 如果取得记录
        tkinter.messagebox.showinfo(title='Python tkinter', message='OK')
    else:
        tkinter.messagebox.showerror('Python tkinter', message='Error')


def cancel():  # 取消按钮的事件处理函数
    varName.set('')
    varPwd.set('')


# 创建按钮组件，同时设置按钮事件处理函数
buttonOk = tkinter.Button(win, text='Login', command=login)
buttonOk.place(x=30, y=70, width=50, height=20)
buttonCancel = tkinter.Button(win, text='Reset', command=cancel)
buttonCancel.place(x=90, y=70, width=50, height=20)
win.mainloop()  # 启动消息循环
