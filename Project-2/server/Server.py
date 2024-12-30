import socket

ADDR = socket.gethostbyname(socket.gethostname())
PORT = 8080

def start_server(host=ADDR, port=PORT):
    # making sure we're using tcp and ipv4
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # binding the socket to the host and port
        s.bind((host, port))
        # listening for incoming connections
        s.listen(5)
        # printing the host and port
        print(f'Server listening on {host}:{port}')
        
        while True:
            conn, addr = s.accept()
            with conn:
                print(f'Connected by {addr}')
                request = conn.recv(1024).decode()
                print(f'Received request: {request}')
                
                # Simple HTTP response
                response = """\
HTTP/1.1 200 OK

Hello, World!
"""
                conn.sendall(response.encode())
                conn.close()

if __name__ == "__main__":
    start_server()