# Chat-Application
A Chat Application Using Python With AES Encryption 

 
# Requirements:
pyaes module - for pure python AES implementation 

# Module Installation :

'''bash
pip install pyaes
'''

Server side :

'''bash
python3 Server.py
’''
  
Client Side : 
'''bash

python3 Client.py
'''

Chat With Users Using their IP Address and Port Number Chosen to Communicate. (Kinda Like netcat)

Server must be Running, Otherwise the connection will be refused

Should work out of the box, atleast for device on LAN

Have Fun!

It uses Sockets to communicate and also has threading so you can recieve messages while you send messages!

# Future : 
1. Having a key exchange mechanism like diffie-hellman key exchange or key exchange using RSA public key encryption to exchange keys securely without needing to use hash of pre-shared-key .
2. Sending hash of message string to later check the data integrity and dislay only verified messages.
3. Sending Data files or some other data ..
