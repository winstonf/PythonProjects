from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext 
import threading
import queue
from tcp_server_v1 import TCP_Server
class MainWindow:
        
        def __init__(self, master):
                self.master = master
                self.master.title("TCP Server Demo")
                self.mylabel = Label(master,text="TCP Server",padx=20, pady=10).grid(row=0, column= 0)
                self.mylabel2 = Label(master, text="Server Connected", padx=20, pady=10).grid(row = 1, column=0)

                self.button1 = Button(master, text="Send Value", command = self.buttonClick).grid(row=1, column=1)

                self.pbar = ttk.Progressbar(orient = "horizontal", length = 350, mode="determinate", maximum="100", value = "25").grid(row = 3, column=0 , columnspan = 2) 

                self.TBox = Entry(master, borderwidth=2, fg="blue", bg= "#ffffb3")
                self.TBox.grid(row=0,column=1)

                self.text_area = scrolledtext.ScrolledText(master, wrap = WORD, width = 40, height = 10, font = ("Times New Roman", 15)) 
                self.text_area.grid(column = 0, pady = 10, padx = 10 , columnspan = 2) 
                # text_area.configure(state ='disabled') 
        
        def buttonClick(self):
                self.text_area.insert(INSERT, self.TBox.get())


root = Tk()
ui = MainWindow(root)
root.mainloop()



