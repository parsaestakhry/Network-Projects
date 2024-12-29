import socket
import random

ADDR = socket.gethostbyname(socket.gethostname())
PORT = 8080
KEYS_FILE =  r'C:\Users\parsa\Desktop\Network-Projects\Project-1\server\keys.txt'

def read_keys(file_path):
    with open(file_path, 'r') as file:
        keys = file.readlines()
    return [key.strip() for key in keys]

def get_random_key(keys):
    return random.choice(keys)

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
                decoded = data.decode()
                if not data:
                    break
                print(f'Received from client uppercased : {decoded.upper()}')
                random_key = get_random_key(keys)
                print(f'Random key selected: {random_key}')
                conn.sendall(data)

if __name__ == "__main__":
    start_server()