import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and the port that the server will listen to
host = 'localhost'
port = 9999

# Bind to the port
s.bind((host, port))

# Now wait for client connection.
s.listen(5)
print('Server listening...')

while True:
   # Establish connection with client.
   c, addr = s.accept()
   print('Got connection from', addr)

   # send a thank you message to the client.
   c.send('Thank you for connecting'.encode())
   # Close the connection
   c.close()