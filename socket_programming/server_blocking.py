import socket
import time
from threading import Thread

def create_server(port):
    """Creates a server that listens on specified port"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(1)
    print(f"Server started on port {port}")
    
    while True:
        print(f"Waiting for connection on port {port}...")
        client_socket, address = server_socket.accept()  # This blocks until a client connects
        print(f"Got connection on port {port} from {address}")
        
        # Simulate some processing
        time.sleep(2)
        client_socket.close()

def demo_single_thread():
    print("\n=== Starting Single Thread Demo ===")
    print("This will block at first server...")
    
    # Try to create multiple servers in sequence
    create_server(8001)  # This will block here
    print("This line never gets printed!")
    create_server(8002)  # This never gets reached
    create_server(8003)  # This never gets reached

def demo_with_threads():
    print("\n=== Starting Multi-Thread Demo ===")
    print("All servers will start...")
    
    # Create multiple servers using threads
    Thread(target=create_server, args=(8001,)).start()
    Thread(target=create_server, args=(8002,)).start()
    Thread(target=create_server, args=(8003,)).start()

# Test the blocking behavior
if __name__ == "__main__":
    print("Choose demo to run:")
    print("1. Single Thread Demo (will block)")
    print("2. Multi-Thread Demo (will work)")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == "1":
        demo_single_thread()
    else:
        demo_with_threads()