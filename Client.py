# CLIENT CODE
# Update 1.1 AES Encryption Now Included :p
# AES Block Cipher 16 bytes block size as supported by pyaes
# Server Code Must Be Running Before Starting Client or Connection will be refused
# Author : xtreme.research@gmail.com

import os
try:
    import pyaes # run : $ pip install pyaes
except ImportError:
    print("Install pyaes library!")
    print("windows : python -m pip insatll pyaes")
    print("linux   : pip install pyaes ")
    exit()
import socket
import threading
import hashlib

print("[+] Client Running ")
HOST = str(input("[+] Enter Destination IP : "))
PORT = int(input("[+] Enter Port : "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

key = str(input("Enter AES Encryption Key For Connection : "))
hashed = hashlib.sha256(key.encode()).digest()
aes = pyaes.AES(hashed)

def process_bytes(bytess):
    ret = []
    while(len(bytess)>=16):
        if(len(bytess)>=16):
            byts = bytess[:16]
            ret.append(byts)
            bytess = bytess[16:]
        else:
            print("Block Size Mismatch ")
    return ret
def process_text(data): #take data in as a string return 16 bytes block of bytes list
    streams = []
    while (len(data)>0):
        if(len(data)>=16):
            stream = data[:16]
            data = data[16:]
        else:
            stream = data + ("~"*(16-len(data)))
            data = ''
        stream_bytes = [ ord(c) for c in stream]
        streams.append(stream_bytes)
    return streams

class myThread(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.threadID = id
        
    def stop(self):
        self.is_alive = False
        
    def run(self):
        print("[+] Listening On Thread "+str(self.threadID))
        while 1:
            data = s.recv(1024)
            if(data!=""):
                processed_data = process_bytes(data)
                print("Recieved : ",end="")
                for dat in processed_data:
                    decrypted = aes.decrypt(dat)
                    mess=''
                    for ch in decrypted:
                        if(chr(ch)!='~'):
                            mess+=str(chr(ch))
                    print (str(mess),end= "")
                print("")

Listening_Thread = myThread(1)
Listening_Thread.daemon = True
Listening_Thread.start()

while 1:
    sending_data = str(input(""))
    if(sending_data=="quit()"):
        Listening_Thread.stop()
        s.close()
        exit()
    sending_bytes = process_text(sending_data)
    enc_bytes = []
    for byte in sending_bytes:
        ciphertext = aes.encrypt(byte)
        enc_bytes += bytes(ciphertext)
    #print("Sending : "+str(sending_data))
    s.send(bytes(enc_bytes))
s.close() #code never reaches here , but just in case ... :p
