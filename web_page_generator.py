import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(900, 200))
        self.master.title("Web Page Generator")
        #default button
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row= 5, column= 4, padx=(10,10), pady=(10,10))

        self.btn1 = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.get_data)
        self.btn1.grid(row= 5, column= 5, padx=(10,10), pady=(10,10))
        
        #display entry field
        tk.Label(self.master, text="Enter custom text or click the Default HTML page button").grid(row = 3, column = 0)

        self.Entry1 = Entry(self.master, textvariable = 'Enter here:', width=100)
        self.Entry1.grid(row= 4, column= 0, padx = 10, columnspan= 30)
    #functionality to default html button
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def get_data(self):
        htmlText = self.Entry1.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        
        






if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
