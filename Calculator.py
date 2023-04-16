from tkinter import *

window=Tk()
window.title("Calculator")
window.resizable(False,False)
window.configure(bg="white")

txt=StringVar()
value=""
def press(num):
        global value
        value = value + str(num)
        txt.set(value)
def calculate():
    try:
        global value
        result=str(eval(value))
        txt.set(result)
    except ZeroDivisionError:
        txt.set("Error")
def all_clear():
    global value
    value=""
    txt.set("")
def clear():
    txt.set(txt.get()[:-1])

entry=Entry(window,textvariable=txt,font=("Times New Roman",42),bg="wheat4",fg="black",bd=5).grid(columnspan=5,sticky='ew')

btn7=Button(window,text='7',width=14,height=2,font=("Times New Roman",14),bg="black",fg="white",command=lambda:press(7))
btn8=Button(window,text='8',width=14,height=2,font=("Times New Roman",14),bg="black",fg="white",command=lambda:press(8))
btn9=Button(window,text='9',width=14,height=2,font=("Times New Roman",14),bg="black",fg="white",command=lambda:press(9))

btn4=Button(window,text='4',width=14,height=2,font=("Times New Roman",14),bg="black",fg="white",command=lambda:press(4))
btn5=Button(window,text='5',width=14,height=2,font=("Times New Roman",14),bg="black",fg="white",command=lambda:press(5))
btn6=Button(window,text='6',width=14,height=2,font=("Times New Roman",14),bg="black",fg="white",command=lambda:press(6))

btn1=Button(window,text='1',width=14,height=2,font=("Times New Roman",14),bg="black",fg="white",command=lambda:press(1))
btn2=Button(window,text='2',width=14,height=2,font=("Times New Roman",14),bg="black",fg="white",command=lambda:press(2))
btn3=Button(window,text='3',width=14,height=2,font=("Times New Roman",14),bg="black",fg="white",command=lambda:press(3))

btndot=Button(window,text='.',width=14,height=2,font=("Times New Roman",14),bg="black",fg="white",command=lambda:press("."))
btn0=Button(window,text='0',width=14,height=2,font=("Times New Roman",14),bg="black",fg="white",command=lambda:press(0))
btneql=Button(window,text='=',width=29,height=2,font=("Times New Roman",14),bg="black",fg="white",command=lambda:calculate())

btnac=Button(window,text='ac',width=14,height=2,font=("Times New Roman",14),bg="red",fg="white",command=lambda:all_clear())
btnc=Button(window,text='c',width=14,height=2,font=("Times New Roman",14),bg="black",fg="white",command=lambda:clear())
btnp=Button(window,text='%',width=14,height=2,font=("Times New Roman",14),bg="black",fg="white",command=lambda:press("%"))
btnd=Button(window,text='/',width=14,height=2,font=("Times New Roman",14),bg="black",fg="white",command=lambda:press("/"))
btnm=Button(window,text='x',width=14,height=2,font=("Times New Roman",14),bg="black",fg="white",command=lambda:press("*"))
btns=Button(window,text='-',width=14,height=2,font=("Times New Roman",14),bg="black",fg="white",command=lambda:press("-"))
btna=Button(window,text='+',width=14,height=2,font=("Times New Roman",14),bg="black",fg="white",command=lambda:press("+"))


btn7.grid(row=4,column=1)
btn8.grid(row=4,column=2)
btn9.grid(row=4,column=3)
btn4.grid(row=5,column=1)
btn5.grid(row=5,column=2)
btn6.grid(row=5,column=3)

btn1.grid(row=6,column=1)
btn2.grid(row=6,column=2)
btn3.grid(row=6,column=3)

btndot.grid(row=7,column=1)
btn0.grid(row=7,column=2)
btneql.grid(row=7,column=3,columnspan=2)

btnac.grid(row=3,column=1)
btnc.grid(row=3,column=2)
btnp.grid(row=3,column=3)
btnd.grid(row=3,column=4)
btnm.grid(row=4,column=4)
btns.grid(row=5,column=4)
btna.grid(row=6,column=4)

label=Label(window,text="Developed by Fouzan M").grid(row=10,column=0,columnspan=5)

window.mainloop()
