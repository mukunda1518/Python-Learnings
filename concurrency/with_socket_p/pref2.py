import time
from socket import *
from threading import Thread

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(("localhost", 25000))


n = 0

def monitor():
    global n
    while True:
        time.sleep(1)
        print(n, "reqs/sec")
        n = 0

Thread(target=monitor).start()


while True:
    sock.send(b"1")
    resp = sock.recv(100)
    n += 1

