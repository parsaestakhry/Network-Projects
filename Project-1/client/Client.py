import socket

ADDR = socket.gethostbyname(socket.gethostname())
PORT = 8080

KEYS_FILE = r"C:\Users\parsa\Desktop\Network-Projects\Project-1\client\keys.txt"


def get_key_value(index):
    with open(KEYS_FILE, "r") as file:
        keys = file.readlines()
    keys = [key.strip() for key in keys]
    for key in keys:
        key_parts = key.split(":")
        if key_parts[0] == index:
            return key_parts[1]


def start_client(host=ADDR, port=PORT):
    # defining the client socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # connecting to the server socket
        s.connect((host, port))
        # printing the connection
        print(f"Connected to server at {host}:{port}")
        while True:
            message = input("Enter message to send (or 'q' to quit): ")
            if message.lower() == "q":
                break
            s.sendall(message.encode())
            data = s.recv(1024)
            decoded = data.decode()

            # Extracting the summed values and index
            response_parts = decoded.split(", Index: ")
            summed_values = response_parts[0].replace("Summed values: ", "")
            summed_values = summed_values.replace("[", "").replace("]", "")
            appended_values = []
            original_values = []
            index = response_parts[1]
            key_value = get_key_value(index)

            for value in summed_values.split(","):
                appended_values.append(int(value))

            for value in appended_values:
                original_value = value - int(key_value)
                original_values.append(original_value)

            original_text = "".join(chr(value) for value in original_values)
            print("*** Decoded message ***")
            print(f"Original text: {original_text}")
            print("***")
            print(f"original_values: {original_values}")
            print(f"appended values: {appended_values}")
            print(f"Index: {index}")
            print(f"Received from server: {decoded}")


if __name__ == "__main__":
    start_client()
