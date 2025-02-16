# Based on this resource - https://newvick.com/python-concurrency/


from socket import * 
from fib import fib
from threading import Thread


def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    print("Srver started on", address)
    while True:
        client, addr = sock.accept()
        print("Connection", addr)
        Thread(target=fib_handler, args=(client, )).start()


def fib_handler(client):
    while True:
        req = client.recv(100)
        if not req:
            break
        result = fib(int(req))
        client.send(str(result).encode() + b"\n")


if __name__ == "__main__":
    fib_server(("", 25000))

        
    
