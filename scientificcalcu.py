from tkinter import *
import math
import parser
import tkinter.messagebox


root = Tk()
root.title("Scientific Calculator")
root.configure(background = 'green')
root.resizable(width=False, height=False)
root.geometry("480x568+0+0")

calc = Frame(root)
calc.grid()
###########*************************

textDisplay = Entry(calc,font=('Helvetica', 20, 'bold'),bg='yellow', bd=30, width=28, justify=RIGHT)
textDisplay.grid(row=0, column=0, columnspan=4,pady=1)
textDisplay.insert(0,"0")



numberpad = "789456123"
i=0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, bg="blue", font=('Helvetica', 20, 'bold'),bd=4,text=numberpad[i]))
        btn[i].grid(row=j,column=k, pady=1)
        i+=1
###########*************************##

btnClear = Button(calc, text=chr(67), width=6, height=2,bg="red", font=('Helvetica', 20, 'bold'),bd=4).grid(row=1, column=0, pady=1)
btnAllClear = Button(calc, text=chr(67)+chr(69), width=6, height=2,bg="red", font=('Helvetica', 20, 'bold'),bd=4).grid(row=1, column=1, pady=1)
btnsq = Button(calc, text="\u221A",width=6, height=2,bg="red", font=('Helvetica', 20, 'bold'),bd=4).grid(row=1, column=2, pady=1)
btnAdd = Button(calc, text="+", width=6, height=2,bg="red", font=('Helvetica', 20, 'bold'),bd=4).grid(row=1, column=3, pady=1)
btnSub = Button(calc, text="-", width=6, height=2,bg="red", font=('Helvetica', 20, 'bold'),bd=4).grid(row=2, column=3, pady=1)
btnMul = Button(calc, text="x", width=6, height=2,bg="red", font=('Helvetica', 20, 'bold'),bd=4).grid(row=3, column=3, pady=1)
btnDiv = Button(calc, text="/", width=6, height=2,bg="red", font=('Helvetica', 20, 'bold'),bd=4).grid(row=4, column=3, pady=1)

btnZero = Button(calc, text="0", width=6, height=2,bg="red", font=('Helvetica', 20, 'bold'),bd=4).grid(row=5, column=0, pady=1)
btnDot = Button(calc, text=".", width=6, height=2,bg="red", font=('Helvetica', 20, 'bold'),bd=4).grid(row=5, column=1, pady=1)
btnPM = Button(calc, text=chr(177), width=6, height=2,bg="red", font=('Helvetica', 20, 'bold'),bd=4).grid(row=5, column=2, pady=1)
btnEquals = Button(calc, text="=", width=6, height=2,bg="red", font=('Helvetica', 20, 'bold'),bd=4).grid(row=5, column=3, pady=1)


###########*************************

btnPi = Button(calc, text="pi", width=6, height=2,bg="red", font=('Helvetica', 20, 'bold'),bd=4).grid(row=1, column=4, pady=1)
btnCos = Button(calc, text="Cos", width=6, height=2,bg="red", font=('Helvetica', 20, 'bold'),bd=4).grid(row=1, column=5, pady=1)
btntan = Button(calc, text="tan", width=6, height=2,bg="blue", font=('Helvetica', 20, 'bold'),bd=4).grid(row=1, column=6, pady=1)
btnsin = Button(calc, text="sin", width=6, height=2,bg="blue", font=('Helvetica', 20, 'bold'),bd=4).grid(row=1, column=7, pady=1)


btn2pi = Button(calc, text="2pi", width=6, height=2,bg="red", font=('Helvetica', 20, 'bold'),bd=4).grid(row=2, column=4, pady=1)
btnCosh = Button(calc, text="Cosh", width=6, height=2,bg="red", font=('Helvetica', 20, 'bold'),bd=4).grid(row=2, column=5, pady=1)
btntanh = Button(calc, text="tanh", width=6, height=2,bg="blue", font=('Helvetica', 20, 'bold'),bd=4).grid(row=2, column=6, pady=1)
btnsinh = Button(calc, text="sinh", width=6, height=2,bg="blue", font=('Helvetica', 20, 'bold'),bd=4).grid(row=2, column=7, pady=1)


btnlog = Button(calc, text="log", width=6, height=2,bg="red", font=('Helvetica', 20, 'bold'),bd=4).grid(row=3, column=4, pady=1)
btnExp = Button(calc, text="exp", width=6, height=2,bg="red", font=('Helvetica', 20, 'bold'),bd=4).grid(row=3, column=5, pady=1)
btntMod = Button(calc, text="Mod", width=6, height=2,bg="blue", font=('Helvetica', 20, 'bold'),bd=4).grid(row=3, column=6, pady=1)
btnE = Button(calc, text="e", width=6, height=2,bg="blue", font=('Helvetica', 20, 'bold'),bd=4).grid(row=3, column=7, pady=1)



btnlog10 = Button(calc, text="log10", width=6, height=2,bg="red", font=('Helvetica', 20, 'bold'),bd=4).grid(row=4, column=4, pady=1)
btncos = Button(calc, text="log1p", width=6, height=2,bg="red", font=('Helvetica', 20, 'bold'),bd=4).grid(row=4, column=5, pady=1)
btnexpm1 = Button(calc, text="expm1", width=6, height=2,bg="blue", font=('Helvetica', 20, 'bold'),bd=4).grid(row=4, column=6, pady=1)
btngamma = Button(calc, text="gamma", width=6, height=2,bg="blue", font=('Helvetica', 20, 'bold'),bd=4).grid(row=4, column=7, pady=1)



btnlog2 = Button(calc, text="log2", width=6, height=2,bg="red", font=('Helvetica', 20, 'bold'),bd=4).grid(row=5, column=4, pady=1)
btndeg = Button(calc, text="deg", width=6, height=2,bg="red", font=('Helvetica', 20, 'bold'),bd=4).grid(row=5, column=5, pady=1)
btnacosh = Button(calc, text="acosh", width=6, height=2,bg="blue", font=('Helvetica', 20, 'bold'),bd=4).grid(row=5, column=6, pady=1)
btnasinh = Button(calc, text="asinh", width=6, height=2,bg="blue", font=('Helvetica', 20, 'bold'),bd=4).grid(row=5, column=7, pady=1)

###########*************************

lbldisplay = Label(calc, text="Scientific calculator",font=('Helvetica', 20, 'bold'),fg='green',justify=CENTER)
lbldisplay.grid(row=0,column=4,columnspan=4)


###########*************************

def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Do you want to exit ?")
    if iExit>0:
        root.destroy()
        return

                                        
def scientific():
    
    root.resizable(width=False, height=False)
    root.geometry("944x568+0+0")
def standard():
    
    root.resizable(width=False, height=False)
    root.geometry("480x568+0+0")

menubar = Menu(calc)

filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = "Standard", command= standard)
filemenu.add_command(label = "Scientific", command= scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command= iExit)

editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Edit', menu = editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_separator()
editmenu.add_command(label = "Paste")


root.config(menu = menubar)

root.mainloop()
