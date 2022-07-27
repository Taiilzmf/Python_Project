#Author Shaelynn Caltagirone
#Create very simple student tracking app




from tkinter import *
import tkinter as tk
from tkinter import messagebox

import student_gui
import student_func

class  ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,300) 
        self.master.maxsize(500,300)

        self.master.title("Student Tracking")

        student_gui.load_gui(self)




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
