import socket

host = '127.0.0.1'
port = 1235

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "hello world"
client_socket.sendto(message.encode(), (host, port))

data, _ = client_socket.recvfrom(1024)
print("Server message:", data.decode())

client_socket.close()
