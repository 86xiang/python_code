from tkinter import *


def computing():
    n1 = int(number1.get())
    n2 = int(number2.get())
    if n1 < n2: n1, n2 = n2, n1
    t = n1 * n2
    temp = n1 % n2
    while temp != 0:
        n1 = n2
        n2 = temp
        temp = n1 % n2
    result = "最小公倍数是：" + str(t / n2)
    label3.config(text=result)


win = Tk()
win.title("最小公倍数")
win.geometry("300x350")
label1 = Label(win, text='请输入数值1：')
label1.config(width=16, height=3)
label1.config(font=('宋体', 12))
label1.grid(row=0, column=0)
number1 = StringVar()
txt1 = Entry(win, textvariable=number1, width=16)
txt1.grid(row=0, column=1)
label0 = Label(win, text='请输入数值2：')
label0.config(width=16, height=3)
label0.config(font=('宋体', 12))
label0.grid(row=1, column=0)
number2 = StringVar()
txt2 = Entry(win, textvariable=number2, width=16)
txt2.grid(row=1, column=1)
label2 = Label(win, text='请单击确认：')
label2.config(width=14, height=3)
label2.config(font=('宋体', 12))
label2.grid(row=2, column=0)
button1 = Button(win, text="计算")
button1.config(justify=CENTER)  #
button1.config(width=14, height=2)  #
button1.config(bd=3, relief=RAISED)  #
button1.config(anchor=CENTER)  #
button1.config(font=('隶书', 12))
button1.config(command=computing)
button1.grid(row=2, column=1)
label3 = Label(win, text='显示结果')
label3.config(width=22, height=3)
label3.config(font=('宋体', 12))
label3.place(x=50, y=230)
win.mainloop()
