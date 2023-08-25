# Commentout to run fun facts
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(("localhost", 9999))
# s.listen(1)
#This will start a socket server on localhost, port 9999

#Fun Facts
#Commment out Previos script
#Start sample-4-server.py first, then run this script
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 9999))
s.sendall(b'Hello, world')
data = s.recv(1024)
s.close()
print('Received', repr(data))
# This will connect to a socket server on localhost, port 9999, send a message, and print the response
