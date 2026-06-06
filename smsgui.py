from uuid import uuid4
import tkinter as tk

class StudentManagementSystem:
    
    def add_data(self,name,roll,year):
        id = str(uuid4())
        data = f"{id},{name},{roll},{year}\n"
        with open("records.txt","a") as db:
            db.write(data)
            db.close()
        display_data_table()
        name_entry_var.set("")
        roll_entry_var.set("")
        year_entry_var.set("")
        
sms = StudentManagementSystem()

root = tk.Tk()
root.title("Student Management System")

root.geometry("700x400")

def display_data_table():
    with open("records.txt","r") as db:
        lines = db.readlines()
        for i in range(0,len(lines)):
            tk.Label(text=lines[i].split(",")[0]).grid(row=5+i,column=0)
            tk.Label(text=lines[i].split(",")[1]).grid(row=5+i,column=1)
            tk.Label(text=lines[i].split(",")[2]).grid(row=5+i,column=2)
            tk.Label(text=lines[i].split(",")[3]).grid(row=5+i,column=3)
        db.close()

name_entry_var = tk.StringVar()
roll_entry_var = tk.StringVar()
year_entry_var = tk.StringVar()

name_lable = tk.Label(root,text="Student Name")
name_lable.grid(row=0,column=0)
name_entry = tk.Entry(root,textvariable=name_entry_var,width=20,justify="left",font=("Arial", 16))
name_entry.grid(row=0,column=1)

roll_lable = tk.Label(root,text="Student Roll")
roll_lable.grid(row=1,column=0)
roll_entry = tk.Entry(root,textvariable=roll_entry_var,width=20,justify="left",font=("Arial", 16))
roll_entry.grid(row=1,column=1)

year_lable = tk.Label(root,text="Student Year")
year_lable.grid(row=2,column=0)
year_entry = tk.Entry(root,textvariable=year_entry_var,width=20,justify="left",font=("Arial", 16))
year_entry.grid(row=2,column=1)

add_atudent_btn = tk.Button(text="Add Student",
        command=lambda: sms.add_data(name_entry_var.get(),roll_entry_var.get(),year_entry_var.get()),
    ).grid(row=3,column=0,columnspan=2)

tk.Label(text="ID").grid(row=4,column=0)
tk.Label(text="NAME").grid(row=4,column=1)
tk.Label(text="ROLL").grid(row=4,column=2)
tk.Label(text="YEAR").grid(row=4,column=3,padx=100)

display_data_table()

root.mainloop()