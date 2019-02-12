import socket
PORT = 8080
IP = "212.128.253.64"

while True:
    msg = input('Enter a message')

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.connect((IP,PORT))

#here we are sending info to the server
    s.send(str.encode(msg))


#here we are able to receive info from the server
    data = s.recv(2048).decode('UTF-8')

    print(msg)
    print('Message from the client')

    s.close()