from tkinter import *
'''
win=Tk()
win.geometry('800x600')
win.title('Windows1')
label1=Label(win,text='Hello Pyhton',anchor='nw')
label1.pack()

label2=Label(win,bitmap='question')
label2.pack()

global png
png=PhotoImage('F:\图片\大强.jpeg')
label3=Label(win,image=png)

label3.pack()
win.mainloop()
'''
s
def GUI(win):
    win.geometry('800x600')
    win.title('Windows1')
    label1 = Label(win, text='Hello Pyhton', anchor='nw')
    label1.pack()

    label2 = Label(win, bitmap='question')
    label2.pack()

    global png
    png = PhotoImage('F:\图片\满意.jpg')
    label3 = Label(win, image=png)
    label3.pack()
    win.mainloop()


win=Tk()
GUI(win)

