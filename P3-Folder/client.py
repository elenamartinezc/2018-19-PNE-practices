import socket

# SERVER IP, PORT
IP = "127.0.0.1"
PORT = 8090



while True:

    # Before connecting to the server, ask the user for the string
    sent = ''
    msg = str(input("> "))
    while len(msg) > 0:
        sent = sent + msg + '\n'
        msg = str(input(''))

    if (len(sent)==0):
        sent = '\n'

    # Now we can create the socket and connect to the servewr
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(sent))

    # Receive the servers respoinse
    answer = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(answer))

    s.close()