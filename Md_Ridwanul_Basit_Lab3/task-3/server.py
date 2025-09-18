import socket
import threading

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

def handle_clients(conn, addr):
    
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
                vowels = "AEIOUaeiou"
                count = 0
                for i in msg:
                    if i in vowels:
                        count += 1
                if count == 0:
                    conn.send("Not enough vowels I guess".encode(FORMAT))
                elif count <= 2:
                    conn.send("Enough vowels I guess".encode(FORMAT))
                else:
                    conn.send("Too many vowels".encode(FORMAT))

    conn.close()

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target= handle_clients, args=(conn, addr))
    thread.start()


