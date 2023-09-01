import socket

HOST = 'localhost' 
PORT = 7590
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_client:
    s_client.connect((HOST, PORT))
    s_client.sendall(b'I like Python')
    data = s_client.recv(1024)

print('Received data: ', repr(data))