import socket
ADDR = socket.gethostbyname(socket.gethostname())
PORT = 8080
def start_client(host=ADDR, port=PORT):\
    # defining the client socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # connecting to the server socket
        s.connect((host, port))
        # printing the connection
        print(f'Connected to server at {host}:{port}')
        while True:
            message = input("Enter message to send (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break
            s.sendall(message.encode())
            data = s.recv(1024)
            print(f'Received from server: {data.decode()}')

if __name__ == "__main__":
    start_client()