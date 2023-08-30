import socket

HOST = 'localhost'
PORT = 7575

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_s:
    client_s.sendto(b"Hello, server!", (HOST, PORT))
    data = client_s.recv(1024)
print('Received', repr(data))