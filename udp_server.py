import socket

host = '127.0.0.1'
port = 1235

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((host, port))

print("Server is listening on port", port)

data, address = server_socket.recvfrom(1024)
text = data.decode()
print("Client message:", text)

reply = text.upper()
server_socket.sendto(reply.encode(), address)

server_socket.close()
