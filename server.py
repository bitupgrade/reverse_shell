import socket
import sys
import threading
import time
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_addresses = []


# Create socket
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Bind socket to port and wait for connection from client
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:  # Binding will keep retrying until successful
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        socket_bind()


'''
# Establish connection with client
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established | " + "IP " +
          address[0] + " | Port " + str(address[1]))
    send_commands(conn)
    conn.close()


# Send commands


def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            # 1024 is the buffer size and has utf-8 encoding
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")
'''

# Accept connections from multiple clients and save to list


def accept_connections():
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_addresses[:]
    while True:
        try:
            conn, address = s.accept()
            conn.setblocking(1)
            all_connections.append(conn)
            all_addresses.append(address)
            print("\nConncetion has been established: " + address[0])
        except:
            print("Error accepting connections")

# Interactive prompt for sending commands reotely


def start_shelly():
    while True:
        cmd = input('shelly>> ')
        if == 'list':
            list_connections()
        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_target_commands(conn)
        else:
            print("Command not recognized")


def main():
    socket_create()
    socket_bind()
    # socket_accept()


main()
