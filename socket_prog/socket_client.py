# echo-client.py
import socket

host = "127.0.0.1"  # The server's hostname or IP address
port = 65432  # The port used by the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def main():
    client.connect((host, port))
    client.send("CLIENT SEND".encode())
    print(client.recv(1024).decode())

main()