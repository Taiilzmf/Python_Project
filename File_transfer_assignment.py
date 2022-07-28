import tkinter as tk
from tkinter import * #importing tkinter module

#setting up GUI window
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #sets title
        self.master.title ("File Transfer")
        #creates select files button from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20)
        #positions source button using grid
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        #creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #positions entry in GUI using tkinter grid() padx and pady are same
        #as button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        #creates button to select destination of files from destination directory
        self.destDir_btn = Button(text= "Select Destination", width=20)
        #positions destination button on next row under source
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        #creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #Positions entry in GUI using tkinter grid to ensure line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))














if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

