from DataStructure import Transmitter
from DataStructure import Reciever
import time

Tx = Transmitter('127.0.0.1',5550)
Tx.start()