from tkinter import *
from tkinter import ttk
root = Tk()
e = Entry(root, width=35, borderwidth = 5)
e.grid(row=0, column=0, columnspan=3,padx= 10, pady= 10)
frame = ttk.Frame(root,padding =10)
frame.grid()

def buttonClick(number):
   #e.delete(0,END)
   current = e.get()
   e.delete (0,END)
   e.insert(0, str(current) + str(number))

def  buttonClear():
   e.delete(0,END)

def buttonAdd():
   firstNumber = e.get()
   #global makes that this instantiation can be used outside
   global f_num
   global math 
   math = "addition"
   f_num = int(firstNumber)
   e.delete(0,END)

def buttonEqual():
   secondNumber =e.get()
   e.delete(0,END)
   if math == "addition":
    e.insert(0,f_num + int (secondNumber))
   if math == "subtraction":
    e.insert(0,f_num - int (secondNumber))
   if math == "divition":
    e.insert(0,int(int(f_num) / int (secondNumber)))
   if math == "Multiplication":
    e.insert(0,int(f_num) * int (secondNumber))

def buttonSub():
    firstNumber = e.get()
   #global makes that this instantiation can be used outside
    global f_num
    global math 
    math = "subtraction"
    f_num = int(firstNumber)
    e.delete(0,END)

def buttonDiv():
    firstNumber = e.get()
   #global makes that this instantiation can be used outside
    global f_num
    global math 
    math = "divition"
    f_num = int(firstNumber)
    e.delete(0,END)
def buttonMult():
    firstNumber = e.get()
   #global makes that this instantiation can be used outside
    global f_num
    global math 
    math = "Multiplication"
    f_num = int(firstNumber)
    e.delete(0,END)
   
ttk.Button (frame, text = 7 , command = lambda: buttonClick(7)).grid(column =1, row=2)
ttk.Button (frame, text = 8, command = lambda: buttonClick(8)).grid(column =2, row=2)
ttk.Button (frame, text = 9 , command = lambda: buttonClick(9)).grid(column =3, row=2)
ttk.Button (frame, text = 4 , command = lambda: buttonClick(4)).grid(column =1, row=3)
ttk.Button (frame, text = 5 , command = lambda: buttonClick(5)).grid(column =2, row=3)
ttk.Button (frame, text = 6, command = lambda: buttonClick(6)).grid(column =3, row=3)
ttk.Button (frame, text = 1 , command = lambda: buttonClick(1)).grid(column =1, row=4)
ttk.Button (frame, text = 2 , command = lambda: buttonClick(2)).grid(column =2, row=4)
ttk.Button (frame, text = 3 , command = lambda: buttonClick(3)).grid(column =3, row=4)
ttk.Button (frame, text = "+" , command = buttonAdd).grid(column =4, row=1)
ttk.Button (frame, text = "-" , command = buttonSub).grid(column =4, row=2)
ttk.Button (frame, text = "=" , command = buttonEqual).grid(column =3, row=5)
ttk.Button (frame, text = "/" , command = buttonDiv).grid(column =4, row=4)
ttk.Button (frame, text = "*" , command = buttonMult).grid(column =4, row=3)
ttk.Button (frame, text = 0 , command = lambda: buttonClick(0)).grid(column =2, row=5)
ttk.Button (frame, text = "clear" , command = buttonClear).grid(column =1, row=5)
ttk.Button (frame,text= "Quit",command =root.destroy).grid(column=4,row=5)
root.mainloop()
