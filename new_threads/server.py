import socket
import threading

HOST = 'localhost' 
PORT = 7590

def handle_client(client_socket):
    print(f"Connecting: {client_socket.getpeername()}")
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.send(data)
    print(f"Disconnecting: {client_socket.getpeername()}")
    client_socket.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print("Server is listening on:", (HOST, PORT))

try:
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()
except KeyboardInterrupt:
    print("Down '")
finally:
    server_socket.close()