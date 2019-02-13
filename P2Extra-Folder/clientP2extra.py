import socket
from Seq import Seq

IP = "212.128.253.84"
PORT = 8081

# We make an infinite loop

while True:
    dna = input('Enter a sequence')
    seq = Seq(dna)

# We create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# We stablish connection
    s.connect((IP,PORT))

# We send data
    s.send(str.encode(dna))


# We receive data
    msg = s.recv(2048).decode('UTF-8')
    print('MESSAGE FROM THE SERVER: \n')
    print(msg)
    s.close()