import tkinter as tk
import math

root = tk.Tk()
root.title("Calculator")

expression = ""

def button_click(value):
    global expression

    if value == "√":
        try:
            number = eval(expression)
            result = math.sqrt(number)
            expression = str(result)
            entry_var.set(expression)
        except Exception:
            expression = ""
            entry_var.set("Error")
    else:
        expression += value
        entry_var.set(expression)

def get_result():
    global expression

    try:
        result = eval(expression)
        expression = str(result)
        entry_var.set(expression)
    except Exception:
        expression = ""
        entry_var.set("Error")

entry_var = tk.StringVar()

entry = tk.Entry(
    root,
    textvariable=entry_var,
    width=20,
    justify="right",
    font=("Arial", 16)
)
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

buttons = [
    (1, 0, "1"),
    (1, 1, "2"),
    (1, 2, "3"),
    (1, 3, "+"),

    (2, 0, "4"),
    (2, 1, "5"),
    (2, 2, "6"),
    (2, 3, "-"),

    (3, 0, "7"),
    (3, 1, "8"),
    (3, 2, "9"),
    (3, 3, "*"),

    (4, 0, "."),
    (4, 1, "0"),
    (4, 2, "="),
    (4, 3, "/"),

    (5, 0, "√"),
]

for row, col, text in buttons:
    if text == "=":
        tk.Button(
            root,
            text=text,
            width=5,
            height=2,
            command=get_result
        ).grid(row=row, column=col, padx=2, pady=2)
    else:
        tk.Button(
            root,
            text=text,
            width=5,
            height=2,
            command=lambda val=text: button_click(val)
        ).grid(row=row, column=col, padx=2, pady=2)

root.mainloop()