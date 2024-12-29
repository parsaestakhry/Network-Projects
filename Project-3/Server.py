import socket
ADDR = socket.gethostbyname(socket.gethostname())
PORT = 8080
def start_server(host=ADDR, port=PORT):
    # making sure we're using tcp and ipv4
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # binding the socket to the host and port
        s.bind((host, port))
        # listening for incoming connections
        s.listen()
        # printing the host and port
        print(f'Server listening on {host}:{port}')
        # 
        conn, addr = s.accept()
        with conn:
            print(f'Connected by {addr}')
            while True:
                data = conn.recv(1024)
                print(f'Received from client: {data.decode()}')
                if not data:
                    break
                conn.sendall(data)

if __name__ == "__main__":
    start_server()