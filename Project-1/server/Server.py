import os
import socket
import random
import sys
import threading

ADDR = socket.gethostbyname(socket.gethostname())
PORT = 8080
KEYS_FILE =  r'C:\Users\parsa\Desktop\Network-Projects\Project-1\server\keys.txt'

def read_keys(file_path):
    with open(file_path, 'r') as file:
        keys = file.readlines()
    return [key.strip() for key in keys]

def get_random_key(keys):
    choice = str(random.choice(keys))
    split_choice = choice.split(":")
    return split_choice

def start_server(host=ADDR, port=PORT):
    keys = read_keys(KEYS_FILE)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f'Server listening on {host}:{port}')
        conn, addr = s.accept()
        with conn:
            print(f'Connected by {addr}')
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                decoded = data.decode()
                ascii_values = [ord(char) for char in decoded]
                print(f'\nASCII values of received data: {ascii_values}')
                
                print(f'Received from client uppercased : {decoded.upper()}')
                random_key = get_random_key(keys)
                random_key_value = int(random_key[1])
                random_key_index = int(random_key[0])
                
                
                summed_values = [value + random_key_value for value in ascii_values]
                print(f'Summed values: {summed_values}')
                
                print(f'Random key selected: {random_key_value} with index {random_key_index}')
                response = f'Summed values: {summed_values}, Index: {random_key_index}'
                conn.sendall(response.encode())
                

            
            
                            
if __name__ == "__main__":
    start_server()