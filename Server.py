#!/usr/bin/python3

# SERVER CODE
# You Can Change the Port Server Listens by passing argument in command line directly
# Server Code To be Started before Client, or Connection will be refused
# NOT SECURE ! Data Can Be easily intercepted using Wireshark or other tools
# DO NOT Transmit Sensitive Data Over this Application !
# Author : xtreme.research@gmail.com

import sys
import socket
import threading

HOST = '0.0.0.0'
if(len(sys.argv)==1):
    PORT = 5559
elif(len(sys.argv)==2):
    PORT=int(sys.argv[1])

print("[+] Server Running ")
print("[+] Allowing All Incoming Connections ")
print("[+] PORT "+str(PORT))
print("[+] Waiting For Connection...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('[+] Connected by ', addr)

class myThread(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.threadID = id

    def run(self):
        print("[+] Listing On Thread "+str(self.threadID))
        while 1:
            data = conn.recv(1024)
            data_recieved = data.decode()
            if(data_recieved != ""):
                print("Recieved : "+str(data_recieved))

Listening_Thread = myThread(1)
Listening_Thread.start()

while 1:
    sending_data = str(input(""))
    conn.send(sending_data.encode())
    #print("Sending : "+str(sending_data))
conn.close()
