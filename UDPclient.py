import socket

# Inisialisasi socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Mengirim data ke server
server_address = ('localhost', 12345)
client_socket.sendto(b"Hello, Server!", server_address)

# Menerima respons dari server
data, server_address = client_socket.recvfrom(1024)
print("Received data from server: {}".format(data.decode('utf-8')))

# Menutup koneksi
client_socket.close()
