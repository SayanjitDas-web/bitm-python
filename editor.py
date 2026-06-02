import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Image editor")

canvas = tk.Canvas(root,width=800,height=600)
canvas.pack()

current_image = None
photo = None

def open_image():
    global current_image, photo
    
    file_path = filedialog.askopenfilename(
        filetypes=[("Images","*.png *.jpg *.jpeg")]
    )
    
    if not file_path:
        return
    
    current_image = Image.open(file_path)
    photo = ImageTk.PhotoImage(current_image)
    
    canvas.delete("all")
    canvas.create_image(0,0,anchor="nw",image=photo)
    
button = tk.Button(root,text="Open Image", command=open_image)
button.pack()

root.mainloop()