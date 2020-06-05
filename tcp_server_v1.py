import socket
import optparse
import time
import sys
import threading as Th


class TCP_Server:
    def __init__(self, host, port, que):
        
        self.serv_port = port
        self.serv_host = host 
        
        print("Initializing TCP Server")
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

    def TCP_Server_Start(self):   
        
        try:
            self.s.bind((self.serv_host, self.serv_port))
            self.s.listen(1)
        except socket.error as msg:
            print("ERROR: ", msg)
            self.s.close()
            self.s = None

        if self.s is None:
            sys.exit(1)

        while 1:
            print("Listening on: %s:%d"%(self.serv_host, self.serv_port))
            self.data_len = 0
            try:
                self.conn, self.addr = self.s.accept()
                print("Start Rx Thread")
                # Rx_Thread = Th.Thread(target= self.TCP_Rx)
                # Rx_Thread.start()
                break
                
            except KeyboardInterrupt:
                print("Closing Connection")
                self.s.close()
                self.s = None
                sys.exit(1)

    def TCP_Tx(self):
        while 1:
            data = input("Enter your option: '1' to turn ON LED, '0' to trun OFF LED and Press the 'Enter' key: ")
            self.conn.send(data.encode())

    def TCP_Rx(self):
        while 1:
            data = self.conn.recv(4096)
            print("")
            if not data: break
            print("Acknowledgement from TCP Client:", data.decode('utf-8'))
            print("")

    def TCP_Close(self):
        print("Closing Connection")
        self.s.close()
        self.s = None
        sys.exit(1)


# Serv = TCP_Server("", 50007)
# Serv.TCP_Tx()

