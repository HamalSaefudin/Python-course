from tkinter import *

root = Tk()

with open("biodata.txt", "r") as f:
    Label(root, text=f.read(), width="25", height="5", justify="left").pack()

root.mainloop()