'''
Program will check if there is connection to a specified host and port.
will return True if there is connection, False if there isn't after timeout has reached 
'''

import socket

host = "8.8.8.8" # server IP address 
port = 53
timeout = 3
def ping():
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # open the socket
        s.connect((host, port)) # send connection request to server
        
    except OSError as e: # If timeout has reached:
        print(e)
        return False
    else: # If connection was succesful 
        s.close()
        print("socket closed")
        return True

try:    
    print(ping())
except KeyboardInterrupt:
    exit("exit")