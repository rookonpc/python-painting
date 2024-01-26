from tkinter import *
from PIL import Image, ImageTk
import os

root = Tk()
root.geometry("800x800")

scriptDir = os.path.dirname(os.path.abspath(__file__))
# print(scriptDir)
img = ImageTk.PhotoImage(Image.open(os.path.join(scriptDir,"realistic-cute-cat-cartoon-style-digital-artwork-free-png.png")))
label = Label(root, image= img)
label.pack()


screen = Canvas(root, width = 400, height = 300)
screen.create_rectangle(0,500,100,100, fill = "grey")
screen.pack()
label.place(relx = 0, rely = 0,anchor= "nw")



mainloop()