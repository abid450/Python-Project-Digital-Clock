# Digital Clock ⏰----------------
import time
from tkinter import *

root=Tk()
root.title("Digital Clock")
root.configure(background="black")

def start():
    Text = time.strftime("%I:%M:%S %p")
    Label.config(text=Text)
    Label.after(1000,start)
Label = Label(root,font=("DS-Digital",100),foreground="cyan",background="black")
Label.pack(anchor="center")
Label.grid(row=0,column=1)
print("Done")
start()
root.mainloop()
