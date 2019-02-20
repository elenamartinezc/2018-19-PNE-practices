import socket
from Seq import Seq

# Configure the Server's IP and PORT
PORT = 8090
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5

# Here is the function for checking if the sequence contains the right characters
def checking(s):
    ok = 'ACGT'
    for letter in s:
        if letter not in ok:
            return False
    return True

# Here is the function for following the command that the user has told us
def command(s1, comando):
    print ('Your command', comando)
    if comando == 'len':
        return s1.len()
    elif comando == 'reverse':
        return s1.reverse().strbase()
    elif comando == 'complement':
        return s1.complement().strbase()
    elif comando == 'countA':
        return s1.count('A')
    elif comando == 'countC':
        return s1.count('C')
    elif comando == 'countG':
        return s1.count('G')
    elif comando == 'countT':
        return s1.count('T')
    elif comando == s1.perc ('A'):
        return s1.perc ('A')
    elif comando == s1.perc ('C'):
        return s1.perc ('C')
    elif comando == s1.perc ('G'):
        return s1.perc ('G')
    elif comando == s1.perc ('T'):
        return s1.perc ('T')
    else:
        return 'ERROR'


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    if msg == '\n':
        answer = 'OK'
    else:
        order = msg.split('\n')
        print('Checking', order[0])
        if (checking(order[0])):
            answer = 'OK\n'

            s1 = Seq(order[0])
            for i in range(1,len(order)-1):
                print('Command', i, order [i])
                r = command(s1,order[i])
                answer = answer + str(r) + '\n'

        else:
            answer = 'ERROR'





    # Print the received message, for debugging
    print("Request message: {}".format(msg))

    # Send the msg back to the client (echo)
    cs.send(str.encode(answer))

    # Close the socket
    cs.close()




# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)