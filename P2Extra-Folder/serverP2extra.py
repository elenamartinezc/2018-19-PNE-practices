import socket

IP = "212.128.253.84"
PORT = 8081
MAX_OPEN_REQUESTS = 5
connections = 0


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
# We reserve the port and the IP
    s.bind((IP, PORT))

# Maximum number of requests
    s.listen(MAX_OPEN_REQUESTS)

# We make an inifite loop
    while True:
        # We accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = s.accept()

        # Another connection!e
        connections += 1

        # We print the number of connections
        print("CONNECTION: {}. From the IP: {}".format(connections, address))

        # We receive a message from the client
        dna = clientsocket.recv(2048).decode("utf-8")
        seq = Seq(dna)
        complementSeq = str(seq.complement())
        print("Message from client: {}".format(dna))

        # We send the message back
        message = "Hello from the teacher's server"
        send_bytes = str.encode(message)
        # We must write bytes, not a string
        clientsocket.send(send_bytes)
        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()