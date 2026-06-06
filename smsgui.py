from uuid import uuid4
import tkinter as tk
import os

class StudentManagementSystem:

    def add_data(self, name, roll, year):
        student_id = str(uuid4())
        data = f"{student_id},{name},{roll},{year}\n"

        with open("records.txt", "a") as db:
            db.write(data)

        display_data_table()

        name_entry_var.set("")
        roll_entry_var.set("")
        year_entry_var.set("")


sms = StudentManagementSystem()

root = tk.Tk()
root.title("Student Management System")
root.geometry("1000x600")
root.configure(bg="#f5f5f5")


def display_data_table():
    # Clear old rows
    for widget in scroll_frame.winfo_children():
        widget.destroy()

    if not os.path.exists("records.txt"):
        return

    with open("records.txt", "r") as db:
        lines = db.readlines()

    for i, line in enumerate(lines):
        row = line.strip().split(",")

        bg = "#f8f8f8" if i % 2 == 0 else "#ffffff"

        tk.Label(
            scroll_frame,
            text=row[0],
            width=40,
            bg=bg,
            relief="solid",
            borderwidth=1,
            anchor="w"
        ).grid(row=i, column=0, sticky="nsew")

        tk.Label(
            scroll_frame,
            text=row[1],
            width=20,
            bg=bg,
            relief="solid",
            borderwidth=1
        ).grid(row=i, column=1, sticky="nsew")

        tk.Label(
            scroll_frame,
            text=row[2],
            width=15,
            bg=bg,
            relief="solid",
            borderwidth=1
        ).grid(row=i, column=2, sticky="nsew")

        tk.Label(
            scroll_frame,
            text=row[3],
            width=15,
            bg=bg,
            relief="solid",
            borderwidth=1
        ).grid(row=i, column=3, sticky="nsew")


# ==========================
# Title
# ==========================

tk.Label(
    root,
    text="Student Management System",
    font=("Arial", 22, "bold"),
    bg="#f5f5f5"
).grid(row=0, column=0, columnspan=5, pady=15)

# ==========================
# Form
# ==========================

name_entry_var = tk.StringVar()
roll_entry_var = tk.StringVar()
year_entry_var = tk.StringVar()

tk.Label(
    root,
    text="Student Name",
    font=("Arial", 11, "bold"),
    bg="#f5f5f5"
).grid(row=1, column=0, padx=10, pady=5, sticky="w")

tk.Entry(
    root,
    textvariable=name_entry_var,
    width=25,
    font=("Arial", 12)
).grid(row=1, column=1, padx=10, pady=5)

tk.Label(
    root,
    text="Student Roll",
    font=("Arial", 11, "bold"),
    bg="#f5f5f5"
).grid(row=2, column=0, padx=10, pady=5, sticky="w")

tk.Entry(
    root,
    textvariable=roll_entry_var,
    width=25,
    font=("Arial", 12)
).grid(row=2, column=1, padx=10, pady=5)

tk.Label(
    root,
    text="Student Year",
    font=("Arial", 11, "bold"),
    bg="#f5f5f5"
).grid(row=3, column=0, padx=10, pady=5, sticky="w")

tk.Entry(
    root,
    textvariable=year_entry_var,
    width=25,
    font=("Arial", 12)
).grid(row=3, column=1, padx=10, pady=5)

tk.Button(
    root,
    text="Add Student",
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=15,
    pady=5,
    command=lambda: sms.add_data(
        name_entry_var.get(),
        roll_entry_var.get(),
        year_entry_var.get()
    )
).grid(row=4, column=0, columnspan=2, pady=10)

# ==========================
# Table Header
# ==========================

header = tk.Frame(root, bg="#d9d9d9")
header.grid(row=5, column=0, columnspan=4, sticky="ew", padx=10)

tk.Label(
    header,
    text="ID",
    width=40,
    bg="#d9d9d9",
    font=("Arial", 10, "bold")
).grid(row=0, column=0)

tk.Label(
    header,
    text="NAME",
    width=20,
    bg="#d9d9d9",
    font=("Arial", 10, "bold")
).grid(row=0, column=1)

tk.Label(
    header,
    text="ROLL",
    width=15,
    bg="#d9d9d9",
    font=("Arial", 10, "bold")
).grid(row=0, column=2)

tk.Label(
    header,
    text="YEAR",
    width=15,
    bg="#d9d9d9",
    font=("Arial", 10, "bold")
).grid(row=0, column=3)

# ==========================
# Scrollable Table
# ==========================

canvas = tk.Canvas(root, height=250, bg="white")
scroll_bar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)

scroll_frame = tk.Frame(canvas)

scroll_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
canvas.configure(yscrollcommand=scroll_bar.set)

canvas.grid(row=6, column=0, columnspan=4, sticky="nsew", padx=10)
scroll_bar.grid(row=6, column=4, sticky="ns")

# Mouse wheel scrolling
canvas.bind_all(
    "<MouseWheel>",
    lambda event: canvas.yview_scroll(
        int(-1 * (event.delta / 120)),
        "units"
    )
)

display_data_table()

root.mainloop()