import csv
import os
import socket
from urllib.parse import urlparse, parse_qs

ADDR = socket.gethostbyname(socket.gethostname())
PORT = 8080


def find_from_id(id: int):
    # Find the data from the id
    print(os.getcwd())
    with open("contacts.csv", mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if int(row["contact_id"]) == id:
                return row
    return None


def find_from_name(name: str):
    # Find the data from the name
    with open("contacts.csv", mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row["contact_name"] == name:
                return row
    return None


def find_from_number(number: str):
    # Find all data entries with the given number
    results = []
    with open("contacts.csv", mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row["contact_number"] == number:
                results.append(row)
    return results


def find_from_address(address: str):
    print(address)
    results = []
    with open("contacts.csv", mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row["contact_address"] == address:
                results.append(row)
    return results


def find_from_email(email: str):
    results = []
    with open("contacts.csv", mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row["contact_email"] == email:
                results.append(row)
    return results

def generate_html_table(data_list):
    if not data_list:
        return "<p>No data found</p>"

    table = "<table border='1'>"
    table += "<tr>"
    for key in data_list[0].keys():
        table += f"<th>{key}</th>"
    table += "</tr>"
    for data in data_list:
        table += "<tr>"
        for value in data.values():
            table += f"<td>{value}</td>"
        table += "</tr>"
    table += "</table>"
    return table


def start_server(host=ADDR, port=PORT):
    # making sure we're using tcp and ipv4
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # binding the socket to the host and port
        s.bind((host, port))
        print(os.getcwd())
        # listening for incoming connections
        s.listen(5)
        # printing the host and port
        print(f"Server listening on {host}:{port}")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                request = conn.recv(1024).decode()
                print(f"Received request: {request}")

                # Parse the request line
                request_line = request.splitlines()[0]
                request_method, path, request_version = request_line.split()

                # Parse the query parameters
                parsed_url = urlparse(path)
                query_params = parse_qs(parsed_url.query)

                # Print the query parameters
                print(f"Query parameters: {query_params}")
                if "id" in query_params:
                    id = int(query_params["id"][0])
                    data = find_from_id(id)
                    print(data)

                    response = f"""\
HTTP/1.1 200 OK

<!DOCTYPE html>
<html>
<head>
    <title>ID Page</title>
</head>
<body>
    <h1>This is ID page</h1>
    {generate_html_table([data])}
</body>
</html>
"""

                elif "name" in query_params:
                    name = query_params["name"][0]
                    data = find_from_name(name)
                    print(data)

                    response = f"""\
HTTP/1.1 200 OK

<!DOCTYPE html>
<html>
<head>
    <title>Name Page</title>
</head>
<body>
    <h1>This is Name page</h1>
    {generate_html_table([data])}
</body>
</html>
"""

                elif "number" in query_params:
                    number = query_params["number"][0]
                    data_list = find_from_number(number)
                    print(data_list)
                    response = f"""\
HTTP/1.1 200 OK

<!DOCTYPE html>
<html>
<head>
    <title>Number Page</title>
</head>
<body>
    <h1>This is Number page</h1>
    {generate_html_table(data_list)}
</body>
</html>
"""             
                elif "address" in query_params:
                    address = query_params["address"][0]
                    data_list = find_from_address(address)
                    print(data_list)
                    response = f"""\HTTP/1.1 200 OK

<!DOCTYPE html>
<html>
<head>
    <title>Address Page</title>
</head>
<body>
    <h1>This is Address page</h1>
    {generate_html_table(data_list)}
</body>
</html> """
                elif "email" in query_params:
                    email = query_params["email"][0]
                    data_list = find_from_email(email)
                    print(data_list)
                    response = f"""\HTTP/1.1 200 OK

<!DOCTYPE html>
<html>
<head>
    <title>Email Page</title>
</head>
<body>
    <h1>This is Email page</h1>
    {generate_html_table(data_list)}
</body>
</html> """
                else:
                    response = """\
HTTP/1.1 400 Bad Request

<!DOCTYPE html>
<html>
<head>
    <title>Error</title>
</head>
<body>
    <h1>400 Bad Request</h1>
    <p>Invalid query parameter</p>
</body>
</html>
"""

                conn.sendall(response.encode())


if __name__ == "__main__":
    start_server()
