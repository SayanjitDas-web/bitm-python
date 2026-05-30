import tkinter as tk

addition = 0

root = tk.Tk()
root.title("My App")
root.geometry("500x500")

def updateLable():
    entry.config(textvariable=str(addition))

def button1():
    global addition
    addition += 1
    updateLable()

def button2():
    global addition
    addition += 2
    updateLable()
    
def button3():
    global addition
    addition += 3
    updateLable()
    
def button4():
    global addition
    addition += 4
    updateLable()
    
def button5():
    global addition
    addition += 5
    updateLable()

entry = tk.Entry(root,textvariable=addition)
entry.grid(row=0,column=0)

tk.Button(root,text="1",background="red", command=button1).grid(row=1,column=0,padx=10)

tk.Button(root,text="2",background="red", command=button2).grid(row=1,column=1,padx=10)

tk.Button(root,text="3",background="red", command=button3).grid(row=1,column=2,padx=10)

tk.Button(root,text="4",background="red", command=button4).grid(row=1,column=3,padx=10)

tk.Button(root,text="5",background="red", command=button5).grid(row=1,column=4,padx=10)

root.mainloop()