import socket

# Inisialisasi socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Binding ke alamat dan port tertentu
server_address = ('localhost', 12345)
server_socket.bind(server_address)
print("Server listening on {}:{}".format(*server_address))

while True:
    # Menerima data dari client
    data, client_address = server_socket.recvfrom(1024)
    print("Received data from {}: {}".format(client_address, data.decode('utf-8')))

    # Mengirim respons ke client
    server_socket.sendto(b"Hello, Client!", client_address)
