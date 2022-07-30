import tkinter as tk
from tkinter import * #importing tkinter module
import tkinter.filedialog
import os
import shutil
import datetime

#setting up GUI window
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #sets title
        self.master.title ("File Transfer")
        #creates select files button from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #positions source button using grid
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))
    
        #creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #positions entry in GUI using tkinter grid() padx and pady are same
        #as button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        #creates button to select destination of files from destination directory
        self.destDir_btn = Button(text= "Select Destination", width=20, command=self.destDir)
        #positions destination button on next row under source
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        #creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #Positions entry in GUI using tkinter grid to ensure line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        #Creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #Positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        #Creates exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #positions exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

    #Creates function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #the .delete(0, end) will clear content in entry widget,
        #this allows path to be inserted into the entry widget properly
        self.source_dir.delete(0, END)
        #.insert method will insert user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)

    #Creates function to select destination directory
    def destDir(self):
        selectDestDir= tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0, END)
        self.destination_dir.insert(0, selectDestDir)

    #creates function to transfer files from one dir to another
    def transferFiles(self):
        #gets source directory
        source = self.source_dir.get()
        #gets destination directory
        destination = self.destination_dir.get()
        #gets a list of files in the source directory
        source_files = os.listdir(source)
        #creates path and checks if files have been modified
        path= "C:/Users/shael/OneDrive/Documents/GitHub/Python_Project/File_tracking_assignment/Customer Source"

        modification_time = os.path.getmtime(path)
        Previous_Date = datetime.datetime.today() - datetime.timedelta(days=1)
        if modification_time < Previous_Date: shutil.move(source + '/' + i, destination)
        #runs through each file in the source directory
        for i in source_files:
            #moves each file in the source to  the destination
            shutil.move(source + '/' + i, destination)
            print(i + ' was successfully transferred.')

    def exit_program(self):
        #root is the   m ain GUI window, the Tkinter destroy method
        #tells python tp terminate root.mainloop
        root.destroy()















if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

