import socket
from Seq import Seq

IP = "212.128.253.114"
PORT = 8086

# We make an infinite loop

while True:
    dna = input('Enter a sequence')
    seq = Seq(dna)
    reverseSeq = seq.reverse()
    complementSeq = seq.complement()

# We create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# We stablish connection
    s.connect((IP,PORT))

# We send data
    seq1 = 'The complement seq is:' + complementSeq.strbase
    seq2 = 'The reverse seq is:' + reverseSeq.strbase
    s.send(str.encode(seq1))
    s.send(str.encode(seq2))

# We receive data
    msg = s.recv(2048).decode('UTF-8')
    print('MESSAGE FROM THE SERVER: \n')
    print(msg)
    s.close()



