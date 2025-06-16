import socket

host = '127.0.0.1'
port = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((host, port))
server_socket.listen()

print("Server is listening on port", port)

connection, address = server_socket.accept()

data = connection.recv(1024)
if data:
    text = data.decode()
    print("Client message:", text)

    response = text.upper()
    connection.send(response.encode())

connection.close()
server_socket.close()
