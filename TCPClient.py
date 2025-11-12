import socket

# Inisialisasi socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Menghubungkan ke server
server_address = ('localhost', 12345)
client_socket.connect(server_address)
print("Connected to {}:{}".format(*server_address))

# Mengirim data ke server
client_socket.sendall(b"Hello, Server!")

# Menerima respons dari server
data = client_socket.recv(1024)
print("Received data from server: {}".format(data.decode('utf-8')))

# Menutup koneksi
client_socket.close()
