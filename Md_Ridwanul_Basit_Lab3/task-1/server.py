import socket

FORMAT = 'utf-8'
HEADER = 64

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 7000
DISCONNECT_MSG = 'End'
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
print("SERVER IS STARTING .....")

#listening stage
server.listen()
print("SERVER IS LISTENING ON", SERVER)

#accepting stage

while True:
    conn, addr = server.accept()
    print("CONNECTED TO", addr)
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
                conn.send(f"TERMINATING THE CONNECTION WITH {addr}".encode(FORMAT))
            else:
                print(msg)
                conn.send("MESSAGE RECIEVED".encode(FORMAT))
    conn.close()