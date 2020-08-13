# import tkinter  # 导入Tkinter模块
# win=tkinter.Tk()  # 创建Windows窗口对象
# win.title('first Python GUI 程序')
# win.mainloop()  # 进入消息循环，即显示窗口

# from tkinter import *
# win1=Tk()
# win1.title('GUI Program')
# win1.geometry("800x600")
# # win1. minsize(400,600) 宽度x高度
# # win1. maxsize(800,600)
# win1.mainloop()

# import tkinter  # 导入Tkinter模块
# root=tkinter.Tk()
# root.geometry("800x600")
# root.title('GUI-02')
# label=tkinter.Label(root,text='Hello Python')
# label.pack()  # 将label组件添加到窗口显示
# button1=tkinter.Button(root,text='Button1')  # Button1
# button1.pack(side=tkinter.LEFT)
# button2=tkinter.Button(root,text='BUtton2')
# button2.pack(side=tkinter.RIGHT)
# root.mainloop()


from tkinter import *
root=Tk()
root.geometry('800x600+100+150')
root.title('计算器示例')
# grid布局
l1=Button(root,text='1',width=12,height=4,bg='yellow')
l2=Button(root,text='2',width=12,height=4)
l3=Button(root,text='3',width=12,height=4)
l4=Button(root,text='4',width=12,height=4)
l5=Button(root,text='5',width=12,height=4,bg='blue')
l6=Button(root,text='6',width=12,height=4)
l7=Button(root,text='7',width=12,height=4)
l8=Button(root,text='8',width=12,height=4)
l9=Button(root,text='9',width=12,height=4,bg='green')
l0=Button(root,text='0',width=12,height=4)
lp=Button(root,text='.',width=12,height=4)

l1.grid(row=0,column=0)
l2.grid(row=0,column=1)
l3.grid(row=0,column=2)
l4.grid(row=1,column=0)
l5.grid(row=1,column=1)
l6.grid(row=1,column=2)
l7.grid(row=2,column=0)
l8.grid(row=2,column=1)
l9.grid(row=2,column=2)
l0.grid(row=3,column=0,columnspan=2,sticky=E+W)  # 跨两列，左右贴紧
lp.grid(row=3,column=2,sticky=E+W)
root.mainloop()


