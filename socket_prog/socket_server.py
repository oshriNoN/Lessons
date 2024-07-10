# echo-server
import socket
import threading
import time
import sys

host = "127.0.0.1"
port = 65432
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

global done
def main():
    global done
    while not done:
        client, addr = server.accept()
        client.sendto("SERVER SEND".encode(), addr)
        print(client.recv(1024).decode())
    print("main thread stopped")



def catch():
    global done
    input("Press any key to exit...\n")
    done = True
    print("Catch thread stopped - will stop on next input")

def shutdown():
    server.shutdown(socket.SHUT_RDWR)
    print("Shutdown")
    server.close()
    print("server closed") 
    

if __name__ =="__main__":
    done = False
    t2 = threading.Thread(target=catch)
    t1 = threading.Thread(target=main)
    t1.start()
    t2.start()
    t1.join()  # Wait for main() thread to finish (which it will when done is True)
    t2.join()  # Wait for catch() thread to finish
    exit("All threads stopped, exiting")