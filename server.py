################################################################
# Client-Server Chat Program - SERVER
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

# Used to display instructions when first message is received
first_connect_flag = True

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # Open socket and listen
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Server listening on: localhost on port: {PORT}")

    # Loop to accept connections
    while True:
        connection, address = s.accept()
        with connection:
            print(f"Connected by {address}")
            print("Waiting for message...")

            # Loop to receive and send messages
            while True:

                # Receive message and decode
                received_data = connection.recv(1024)
                if not received_data:
                    break
                received_data_decoded = received_data.decode('UTF-8')

                # Quit if /q command is received
                if received_data_decoded == '/q':
                    s.close()
                    print("Connection closed.  Goodbye.")
                    quit()

                # Print decoded message
                print(received_data_decoded)

                # Initial program instructions
                if first_connect_flag:
                    print("Type /q to quit")
                    print("Enter message to send...")
                    first_connect_flag = False

                # Receive input from user and send to client
                send_data = input(">")
                connection.sendall(bytes(send_data, 'UTF-8'))

                # Quit program if /q command is entered
                if send_data == '/q':
                    print("Connection closed.  Goodbye.")
                    quit()