from tkinter import *
import tkinter.messagebox as msg
root = Tk()
root.title("Mufaddal's Calci")
root.iconbitmap('calci_icon.ico')

# Copyright label
Label(root, text=u'\u00A9' + 'Mufaddal Shakir').grid(row=6,column=3)

def myclick(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def clr():
    e.delete(0, END)

def plus():
    first=e.get()
    global f_num
    global math
    math = 'plus'
    f_num=float(first)
    e.delete(0,END)

def minus():
    first=e.get()
    global f_num
    global math
    math = 'minus'
    f_num=float(first)
    e.delete(0,END)
def mult():
    first=e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num=float(first)
    e.delete(0,END)
def div():
    first=e.get()
    global f_num
    global math
    math = 'division'
    f_num=float(first)
    e.delete(0,END)
def mod():
    first=e.get()
    global f_num
    global math
    math = 'modulus'
    f_num=float(first)
    e.delete(0,END)

def equalto():
    second=e.get()
    e.delete(0,END)

    if math == 'plus':
        e.insert(0,f_num + float(second))
    if math == 'minus':
        e.insert(0,f_num - float(second))
    if math == 'multiplication':
        e.insert(0,f_num * float(second))
    if math == 'division':
        if float(second)==0:
            msg.showinfo("Error","Invalid Syntax")
            clr()
        else:
            e.insert(0,f_num / float(second))
    if math == 'modulus':
        if float(second) == 0:
            msg.showinfo("Error", "Invalid Syntax")
            clr()
        else:
            e.insert(0, f_num % float(second))



# e=Entry(root,width=75,borderwidth=5,bg='light blue')
e=Entry(root,borderwidth=5,bg='light blue',font=('times', 32))
e.grid(row=0,column=0,columnspan=4,ipady=10)



b1=Button(root,text='1',font=20,padx=40,pady=20,borderwidth=5,fg='white',bg='blue',command=lambda:myclick(1))
b2=Button(root,text='2',font=20,padx=40,pady=20,borderwidth=5,fg='white',bg='blue',command=lambda:myclick(2))
b3=Button(root,text='3',font=20,padx=40,pady=20,borderwidth=5,fg='white',bg='blue',command=lambda:myclick(3))
b4=Button(root,text='4',font=20,padx=40,pady=20,borderwidth=5,fg='white',bg='blue',command=lambda:myclick(4))
b5=Button(root,text='5',font=20,padx=40,pady=20,borderwidth=5,fg='white',bg='blue',command=lambda:myclick(5))
b6=Button(root,text='6',font=20,padx=40,pady=20,borderwidth=5,fg='white',bg='blue',command=lambda:myclick(6))
b7=Button(root,text='7',font=20,padx=40,pady=20,borderwidth=5,fg='white',bg='blue',command=lambda:myclick(7))
b8=Button(root,text='8',font=20,padx=40,pady=20,borderwidth=5,fg='white',bg='blue',command=lambda:myclick(8))
b9=Button(root,text='9',font=20,padx=40,pady=20,borderwidth=5,fg='white',bg='blue',command=lambda:myclick(9))
b0=Button(root,text='0',font=20,padx=40,pady=20,borderwidth=5,fg='white',bg='blue',command=lambda:myclick(0))
bclr=Button(root,text='Clear',font=20,padx=82,pady=20,borderwidth=5,fg='white',bg='grey',command=clr)
bmod=Button(root,text='%',font=20,padx=38,pady=20,borderwidth=5,bg='orange',command=mod)
bplus=Button(root,text='+',font=20,padx=40,pady=20,borderwidth=5,bg='orange',command=plus)
bminus=Button(root,text='-',font=20,padx=40,pady=20,borderwidth=5,bg='orange',command=minus)
bmult=Button(root,text='x',font=20,padx=40,pady=20,borderwidth=5,bg='orange',command=mult)
bdiv=Button(root,text='/',font=20,padx=40,pady=20,borderwidth=5,bg='orange',command=div)
bequal=Button(root,text='=',font=20,padx=155,pady=20,borderwidth=10,bg='sky blue',command=equalto)

bclr.grid(row=1,column=0,columnspan=2)
bmod.grid(row=1,column=2)
bdiv.grid(row=1,column=3)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)
bmult.grid(row=2,column=3)

b4.grid(row=3,column=0)
b5.grid(row=3,column=1)
b6.grid(row=3,column=2)
bminus.grid(row=3,column=3)

b1.grid(row=4,column=0)
b2.grid(row=4,column=1)
b3.grid(row=4,column=2)
bplus.grid(row=4,column=3)

b0.grid(row=5,column=0)
bequal.grid(row=5,column=1,columnspan=3)


root.mainloop()