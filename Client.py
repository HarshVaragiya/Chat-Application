#!/usr/bin/python3

# CLIENT CODE
# Server Code Must Be Running Before Starting Client or Connection will be refused
# NOT SECURE ! Data Can Be easily intercepted using Wireshark or other tools
# DO NOT Transmit Sensitive Data Over this Application !
# Author : xtreme.research@gmail.com


import socket
import threading


HOST = '0.0.0.0'
PORT = 5559
print("[+] Client Running ")
HOST = str(input("[+] Enter Destination IP : "))
PORT = int(input("[+] Enter Port : "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

class myThread(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.threadID = id

    def run(self):
        print("[+] Listing On Thread "+str(self.threadID))
        while 1:
            data = s.recv(1024)
            data_recieved = data.decode()
            if(data_recieved!=""):
                print("Recieved : "+str(data_recieved))

Listening_Thread = myThread(1)
Listening_Thread.start()

while 1:
    sending_data = input("")
    sending_bytes = sending_data.encode()
    s.send(sending_bytes)
    #print("Sent : "+str(sending_data))
s.close()
