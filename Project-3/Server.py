import socket

ADDR = socket.gethostbyname(socket.gethostname())
PORT = 8080

def start_server(host=ADDR, port=PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f'Server listening on {host}:{port}')
        
        while True:
            conn, addr = s.accept()
            with conn:
                print(f'Connected by {addr}')
                while True:
                    data = conn.recv(16384)
                    if not data:
                        break
                    conn.sendall(data)

if __name__ == "__main__":
    start_server()
