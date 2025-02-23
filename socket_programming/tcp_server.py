import socket
import threading

class TCPServer:
    def __init__(self, host='127.0.0.1', port=1729):
        """Initialize the server with host and port."""
        self.host = host
        self.port = port
        # Create a TCP socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Allow reuse of address
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind the socket to the address
        self.server_socket.bind((self.host, self.port))

    def handle_client(self, client_socket, addr):
        """Handle individual client connections."""
        print(f"New connection from {addr}")
        
        try:
            while True:
                # Receive data from client
                request = client_socket.recv(1024).decode('utf-8')
                if not request:
                    break
                    
                print(f"Received from {addr}: {request}")
                
                # Process the request and send response
                response = f"Server received: {request}"
                client_socket.send(response.encode('utf-8'))
                
        except Exception as e:
            print(f"Error handling client {addr}: {e}")
        finally:
            client_socket.close()
            print(f"Connection closed with {addr}")

    def start(self):
        """Start the server and listen for connections."""
        # Start listening for connections
        self.server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")
        
        try:
            while True:
                # Accept new connection
                client_socket, addr = self.server_socket.accept()
                # Create new thread to handle client
                client_thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, addr)
                )
                client_thread.start()
                
        except KeyboardInterrupt:
            print("\nShutting down server...")
        finally:
            self.server_socket.close()

# Example usage
if __name__ == "__main__":
    server = TCPServer()
    server.start()