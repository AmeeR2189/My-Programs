import tkinter
def fun():
    d=['']*6
    d[0]=t1.get()
    d[1]=t2.get()
    print(roll,name)
root=tkinter.Tk()
root.geometry('200x150')
t1=tkinter.Entry(root)
t2=tkinter.Entry(root)
t3=tkinter.Entry(root)
t4=tkinter.Entry(root)
t5=tkinter.Entry(root)
t6=tkinter.Entry(root)
b1=tkinter.Button(root,text="submit",command=fun)
t1.pack()
t2.pack()
t3.pack()
t4.pack()
t5.pack()
t6.pack()
b1.pack()


