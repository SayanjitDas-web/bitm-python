import tkinter as tk

root = tk.Tk()
root.title("Calculator")

expression = ""

def button_click(value):
    global expression
    expression += value
    entry_var.set(expression)

def get_result():
    global expression
    try:
        val = eval(expression)
        expression = str(val)
        entry_var.set(expression)
    except:
        expression = ""
        entry_var.set("Error")

entry_var = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_var)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    (1,0,"1"),
    (1,1,"2"),
    (1,2,"3"),
    (1,3,"+"),
    (2,0,"4"),
    (2,1,"5"),
    (2,2,"6"),
    (2,3,"="),
]

for button in buttons:
    if button[2] == "=":
        tk.Button(
            root,
            text=button[2],
            command=get_result
        ).grid(row=button[0], column=button[1])
    else:
        tk.Button(
            root,
            text=button[2],
            command=lambda val=button[2]: button_click(val)
        ).grid(row=button[0], column=button[1])

root.mainloop()