import socket
from socket import AF_INET, SOCK_STREAM


#  Ask OS to create a TCP socket
 
server_socket = socket.socket(AF_INET, SOCK_STREAM)
server_socket.bind(('localhost', 1234))
server_socket.listen()
print("Server started on port 1234")

# Now Nginx just reads and writes HTTP data

while True:
    client_socket, address = server_socket.accept()
    print("Server got a connection from", address)
    
    request = client_socket.recv(1024).decode()
    print(request)
    http_response = "HTTP/1.1 200 OK\r\n..."
    client_socket.send(http_response.encode())
    client_socket.close()
    