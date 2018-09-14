import cv2
import socket
import pickle
import threading

class Transmitter(threading.Thread):
    def __init__(self,ip,port):
        threading.Thread.__init__(self) 
        self.ip = ip
        self.port = port 
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((ip,port))
        self.cam = cv2.VideoCapture(0)

    def run(self):
        while(True):
            try:
                self.ret , self.frame = self.cam.read() 
                self.data = pickle.dumps(self.frame)
                self.sock.send(self.data)
            except:
                print(" -> Broken Pipe ! \n Exiting")
                break
    
    def __del__(self):
        self.sock.close()
        self.cam.release()
        cv2.destroyAllWindows()

class Reciever(threading.Thread):
    def __init__(self,ip,port):
        threading.Thread.__init__(self)
        self.ip   = ip 
        self.port = port
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.bind((ip,port))
        self.sock.listen(1)

    def run(self):
        self.conn , self.addr = self.sock.accept()
        print("Incoming Connection From{}".format(self.addr))
        while(True):
            data = self.conn.recv(921781)
            try:
                frame = pickle.loads(data)
                cv2.imshow('Frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            except:
                pass
    
    def __del__(self):
        self.conn.close()
        self.sock.close()
        cv2.destroyAllWindows()
