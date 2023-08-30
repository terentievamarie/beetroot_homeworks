import socket

HOST = 'localhost' 
PORT = 8000

def get_key():
    key = input("enter key: ")
    return int(key)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_s:
    message = input("Enter message: ")
    client_s.sendto(message.encode('utf-8'), (HOST, PORT))
    key_prompt = client_s.recvfrom(1024)
    key = get_key()
    
    client_s.sendto(str(key).encode('utf-8'), (HOST, PORT))
    
    encrypted_message, _ = client_s.recvfrom(1024)
    print(f'received encrypted message: {encrypted_message.decode("utf-8")}')