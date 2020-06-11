from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext 
import threading
import queue
from tcp_server_v1 import TCP_Server
class MainWindow:
        
        def __init__(self, master):
                
                q = queue.Queue()
                
                Serv = TCP_Server('',50007)
                self.TCP_Server_Init = threading.Thread(target=Serv.TCP_Server_Start,args=(q, ))
                self.TCP_Server_Init.start()
                self.TCP_Server_Init.join()
                TCP_Tx_Thread = threading.Thread(target=Serv.TCP_Tx)
                TCP_Tx_Thread.start()9999999
                TCP_Rx_Thread = threading.Thread(target=Serv.TCP_Rx)
                TCP_Rx_Thread.start()
                # # QueCheckThread = threading.Thread(target=self.QueIndicationsCheck, args=(q, ))
                # # QueCheckThread.start()

                self.master = master
                self.master.title("TCP Server Demo")
                
                self.mylabel_TCP_Mode = Label(master,text="TCP Server Status",padx=10, pady=10).grid(row=0, column= 0)
                self.mylabel_ConnStat = Label(master, text="Disonnected", padx=10, pady=10, fg="red").grid(row = 0, column=1)
                
                self.mylabel_CSlide = Label(master, text="CapSense Slider ", padx=10, pady=10).grid(row = 3, column=0)
                self.Button_SendData = Button(master, text="Send Value", command = self.SendButtonClick).grid(row=1, column=1)

                self.ProgBar_CapSlideDispBar = ttk.Progressbar(orient = "horizontal", length = 200, mode="determinate", maximum="100", value = "25").grid(row = 3, column=1 , columnspan = 1) 

                self.TBox_DataEntry = Entry(master, borderwidth=2, fg="blue", bg= "#ffffb3")
                self.TBox_DataEntry.grid(row=1,column=0)

                self.text_area = scrolledtext.ScrolledText(master, wrap = WORD, width = 40, height = 10, font = ("Times New Roman", 15)) 
                self.text_area.grid(column = 0, pady = 10, padx = 10 , columnspan = 2) 
                # text_area.configure(state ='disabled') 


        def QueIndicationsCheck(self,que):
                print(str(que.qsize()))
                data = que.get()
                # if data == "Socket Connected":
                print(str(que.qsize()))
                print(data)

                # self.text_area.insert(INSERT, data)

        def SendButtonClick(self):
                self.text_area.insert(INSERT, self.TBox_DataEntry.get())
        
        def Conn_Stat_Label(self):
                self.mylabel_ConnStat = Label(master, text="Connected", padx=10, pady=10,fg="Green").grid(row = 1, column=0)


# q = queue.Queue()

root = Tk()
ui = MainWindow(root)
# Serv = TCP_Server('',50007)
# Serv.TCP_Server_Start(q)
# TCP_Tx_Thread = threading.Thread(target=Serv.TCP_Tx)
# TCP_Tx_Thread.start()
# TCP_Rx_Thread = threading.Thread(target=Serv.TCP_Rx)
# TCP_Rx_Thread.start()
root.mainloop()


