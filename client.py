################################################################
# Client-Server Chat Program - CLIENT
# By Casimero Tanseco
#
# Sources:
# 1) https://docs.python.org/3/howto/sockets.html
# 2) https://realpython.com/python-sockets/#socket-api-overview
################################################################

import socket

# Connection details
HOST = "127.0.0.1"
PORT = 65123

# Connect to server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Connected to localhost on port: {PORT}")
    print("Type /q to quit")

    # Loop to send and receive messages from server
    while True:

        # Receive input from user and send message to server
        send_data = input(">")
        s.sendall(bytes(send_data, 'UTF-8'))

        # Quit program if /q command is entered
        if send_data == '/q':
            print("Connection closed.  Goodbye.")
            quit()

        # Receive and decode data from server
        received_data = s.recv(1024)
        if not received_data:
            break
        received_data_decoded = received_data.decode('UTF-8')

        # Quit if /q command is received
        if received_data_decoded == '/q':
            s.close()
            print("Connection closed.  Goodbye.")
            quit()

        # Print decoded message
        print(received_data.decode('UTF-8'))