import socket
import random
from threading import Thread

def create_load_balancer(web_servers):
    """Load Balancer: First point of contact"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8000))  # Main entry point
    server_socket.listen(5)
    print("Load Balancer started on port 8000")
    
    while True:
        client_socket, address = server_socket.accept()
        print(f"New connection from {address}")
        
        # Select a web server using round-robin
        selected_server = web_servers[random.randint(0, len(web_servers)-1)]
        forward_to_web_server(client_socket, selected_server)

def forward_to_web_server(client_socket, web_server):
    """Forwards request from load balancer to web server"""
    try:
        web_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        web_server_socket.connect(web_server)
        
        # Forward client request
        request = client_socket.recv(1024)
        web_server_socket.send(request)
        
        # Get response and send back to client
        response = web_server_socket.recv(1024)
        client_socket.send(response)
        
        client_socket.close()
        web_server_socket.close()
    except Exception as e:
        print(f"Error forwarding to web server: {e}")

def create_web_server(port, app_servers):
    """Web Server: Handles static content and forwards dynamic requests"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(5)
    print(f"Web Server started on port {port}")
    
    while True:
        client_socket, address = server_socket.accept()
        request = client_socket.recv(1024).decode('utf-8')
        
        if 'GET /static/' in request:
            # Handle static content
            response = """HTTP/1.1 200 OK
                Content-Type: text/html

                <html>
                <body>
                <h1>Static Content from Web Server</h1>
                <p>Served directly from Web Server on port {port}</p>
                </body>
                </html>
            """.encode('utf-8')
            client_socket.send(response)
        else:
            # Forward to application server
            selected_app_server = app_servers[random.randint(0, len(app_servers)-1)]
            forward_to_app_server(client_socket, selected_app_server, request)
        
        client_socket.close()

def forward_to_app_server(client_socket, app_server, request):
    """Forwards request from web server to application server"""
    try:
        app_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        app_socket.connect(app_server)
        app_socket.send(request.encode('utf-8'))
        
        response = app_socket.recv(1024)
        client_socket.send(response)
        
        app_socket.close()
    except Exception as e:
        print(f"Error forwarding to application server: {e}")

def create_app_server(port):
    """Application Server: Handles business logic"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(5)
    print(f"Application Server started on port {port}")
    
    while True:
        client_socket, address = server_socket.accept()
        request = client_socket.recv(1024).decode('utf-8')
        
        # Simulate processing and database interaction
        response = f"""HTTP/1.1 200 OK
            Content-Type: text/html

            <html>
            <body>
            <h1>Dynamic Content from Application Server</h1>
            <p>Processed by Application Server on port {port}</p>
            <p>Request path: {request.split()[1]}</p>
            </body>
            </html>
        """
        client_socket.send(response.encode('utf-8'))
        client_socket.close()

def start_system():
    # Define ports
    web_server_ports = [8081, 8082]  # Multiple web servers
    app_server_ports = [9001, 9002]  # Multiple application servers
    
    # Create server lists
    web_servers = [('localhost', port) for port in web_server_ports]
    app_servers = [('localhost', port) for port in app_server_ports]
    
    # Start application servers
    for port in app_server_ports:
        Thread(target=create_app_server, args=(port,)).start()
    
    # Start web servers
    for port in web_server_ports:
        Thread(target=create_web_server, args=(port, app_servers)).start()
    
    # Start load balancer (runs on main thread)
    create_load_balancer(web_servers)

if __name__ == "__main__":
    start_system()