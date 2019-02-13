import socket
from Seq import Seq

IP = "212.128.253.84"
PORT = 8086

# We make an infinite loop

while True:
    dna = input('Enter a sequence')
    seq = Seq(dna)
    reverseSeq = str(seq.reverse())
    complementSeq = str(seq.complement())

# We create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# We stablish connection
    s.connect((IP,PORT))

# We send data
    s.send(str.encode(reverseSeq))
    s.send(str.encode(complementSeq))

# We receive data
    msg = s.recv(2048).decode('UTF-8')
    print('MESSAGE FROM THE SERVER: \n')
    print(msg)
    s.close()



