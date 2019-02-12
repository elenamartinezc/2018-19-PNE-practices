import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print ('Socket connected')

PORT = 8080
IP = "212.128.253.64"

s.connect((IP,PORT))

s.send(str.encode('Hello'))

msg = s.recv(2048).decode('UTF-8')
print('Message from the server')
print (msg)

s.close()

print('The end')