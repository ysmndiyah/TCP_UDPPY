import socket

# Inisialisasi socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding ke alamat dan port tertentu
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Mendengarkan koneksi masuk
server_socket.listen(5)
print("Server listening on {}:{}".format(*server_address))

while True:
    # Menerima koneksi dari client
    client_socket, client_address = server_socket.accept()
    print("Received connection from {}:{}".format(*client_address))

    # Menerima dan mengirim data
    data = client_socket.recv(1024)
    print("Received data: {}".format(data.decode('utf-8')))
    client_socket.sendall(b"Hello, Client!")

    # Menutup koneksi
    client_socket.close()
