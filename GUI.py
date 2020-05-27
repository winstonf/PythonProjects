from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext 


root = Tk()
root.minsize(250, 250) 

TBox = Entry(root, borderwidth=2, fg="blue", bg= "#ffffb3")
TBox.grid(row=0,column=1)

def buttonClick():
        text_area.insert(INSERT, TBox.get())


mylabel = Label(root,text="TCP Server",padx=20, pady=10).grid(row=0, column= 0)
# mylabel.grid(row=0, column= 0)
mylabel2 = Label(root, text="Server Connected", padx=20, pady=10).grid(row = 1, column=0)
# mylabel2.grid(row = 1, column=0)
button1 = Button(root, text="Send Value", command = buttonClick).grid(row=1, column=1)
pbar = ttk.Progressbar(orient = "horizontal", length = 350, mode="determinate", maximum="100", value = "25").grid(row = 3, column=0 , columnspan = 2) 

text_area = scrolledtext.ScrolledText(root, wrap = WORD, width = 40, height = 10, font = ("Times New Roman", 15)) 
text_area.grid(column = 0, pady = 10, padx = 10 , columnspan = 2) 
# text_area.configure(state ='disabled') 

root.mainloop()