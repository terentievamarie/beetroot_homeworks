import socket

HOST = 'localhost'
PORT = 7575

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_s:
    server_s.bind((HOST, PORT))
    while True:
        data = server_s.recvfrom(1024)
        message = data[0]
        address = data[1]
        print(f'Message: {message}, adress: {address}')
        server_s.sendto(b'Hello ,client!', address)