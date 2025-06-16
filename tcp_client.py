import socket

host = '127.0.0.1'
port = 2323

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

message = "hello world"
client_socket.send(message.encode())

reply = client_socket.recv(1024)
print("Server message:", reply.decode())

client_socket.close()
