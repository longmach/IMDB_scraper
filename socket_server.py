import socket
import time
import pickle
from IMDB_Scraper import imdb 

FORMAT = 'utf-8'
HEADER = 64     

print("[STARTING] server is starting...")

#create server and listen
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1243))
s.listen(5)

while True:
    # connect to client socket
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    print("Received request")

    #receive request
    connected = True
    while connected:
        msg = clientsocket.recv(HEADER)
        data = pickle.loads(msg)
        print(data)
        connected = False

    #call IMDB scraper function
    d = imdb(data[0], data[1], data[2])

    #serialize using pick and send
    msg = pickle.dumps(d)
    print("Sending reply")
    clientsocket.send(msg)

    #close connection and back to listen
    print("[Closing] Connection is closed. Server is waiting for a new client...")
    clientsocket.close()
