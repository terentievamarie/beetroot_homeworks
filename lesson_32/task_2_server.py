import socket

HOST = 'localhost'
PORT = 8000

def caesar_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = (ord(char) - ord('a') + key) % 26
            encrypted_char = chr(ord('a') + shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_s:
    server_s.bind((HOST, PORT))
    while True:
        data = server_s.recvfrom(1024)
        message = data[0].decode('utf-8')
        address = data[1]
        print(f'Received message: {message}, Address: {address}')
        
        server_s.sendto(b"Enter key:", address)
        key_data = server_s.recvfrom(1024)
        key = int(key_data[0].decode('utf-8'))

        encrypted_message = caesar_encrypt(message, key)
        server_s.sendto(encrypted_message.encode('utf-8'), address)