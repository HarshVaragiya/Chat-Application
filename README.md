# Chat-Application
A Chat Application Using Python With 256 Bit AES Encryption.

# Requirements:
pyaes module - for pure python AES implementation 
You can use other modules like pycrypto(not recommended because it is vulnerable to attacks, and unmaintained) or pycryptodome (or pycryptodomex),For Cryptography but i wanted to go with simple and pure python implementation. Might switch to pycryptodomex later (if and when required).

# Module Installation :

Installing PyAES Module :
```bash
pip install pyaes
```
# Usage :
The Server Side must be running first.
Server side :
```bash
python3 Server.py
```
Client Side : 
```bash
python3 Client.py
```
Chat With Users Using their IP Address and Port Number Chosen to Communicate. (Kinda Like netcat)
Server must be Running, Otherwise the connection will be refused
Should work out of the box, atleast for device on LAN
Have Fun!

It uses Sockets to communicate and also has threading so you can recieve messages while you send messages!

# Future : 
0. NAT Punching Features, and using a UDP Socket with message integrity verification to pass through some firewalls.
1. Having a key exchange mechanism like diffie-hellman key exchange ( Client1 -> Main-Server -> Client2 Style Centralized System) or key exchange using RSA public key encryption to exchange and verify key and check integrity of keys securely without needing to use hash of pre-shared-key or Central Server (more P2P Style).
Dropping the use of hash of pre-shared-key is a good move because it can be very easy to crack using Rainbow Tables, as it does not use Salting. 
2. Sending hash of message string to later check the data integrity and dislay only verified messages.
3. Sending Data files or some other data ..
4. Using standard AES Block Cipher implementations (still 256 Bits though) as used in PyCryptoDome

# Updates:
1. Added Message Verification to check message integrity, along with message timestamps.
2. Also Solved the problem where Socket Object closes from one end and crashes the other side.
3. Updated Screenshot.
