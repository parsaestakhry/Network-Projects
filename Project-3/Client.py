import socket
import time

ADDR = socket.gethostbyname(socket.gethostname())
PORT = 8080
message_sizes = [1024, 2048, 4096, 8192, 16384]

def start_client(host=ADDR, port=PORT):
    for size in message_sizes:
        message = b"1" * size
        total_rtt = 0
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            print(f'Connected to server at {host}:{port}')

            for i in range(1000):
                start_time = time.time()
                s.sendall(message)
                
                # Receive data in chunks until we get the full message
                received_data = b""
                while len(received_data) < size:
                    chunk = s.recv(size - len(received_data))
                    if not chunk:
                        break
                    received_data += chunk
                    
                end_time = time.time()
                rtt = end_time - start_time
                total_rtt += rtt
                print(f"Message size: {size} bytes")
                print(f"RTT for message {i+1}: {rtt:.6f} seconds")
        average_rtt = total_rtt / 1000
        print(f'average RTT {average_rtt}')

if __name__ == "__main__":
    start_client()
