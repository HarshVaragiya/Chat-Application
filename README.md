# Chat-Application
A Simple Chat Application Using Python

Server side : python3 Server.py  
  
Client Side : python3 Client.py

Chat With Users Using their IP Address and Port Number Chosen to Communicate. (Kinda Like netcat)

Server must be Running, Otherwise the connection will be refused

Should work out of the box, atleast for device on LAN

>> NOT SECURE :
this application is transmitting data in plaintext(encoded text but..) it can be easily intercepted and hence DO NOT Transmit any sensitive data on it!
data can be easily intercepted with wireshark or similar tool.

Have Fun!

It uses Sockets to communicate and also has threading so you can recieve messages while you send messages!
