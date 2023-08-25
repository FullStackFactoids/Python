import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 8080))
s.listen(5)
# This sets up a server socket on port 8080 and listens for connections.

# Fun Facts
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("www.python.org", 80))
    s.sendall(b"GET / HTTP/1.1\r\nHost: www.python.org\r\n\r\n")
    data = s.recv(1024)
print(data)  # Output: HTTP response from www.python.org

