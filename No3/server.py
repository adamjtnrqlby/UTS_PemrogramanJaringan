import socket
import time

HOST = "127.0.0.1"
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server berjalan... menunggu koneksi...")

conn, addr = server.accept()
print("Client terhubung:", addr)

# Delay 4 detik untuk mengetes timeout client
time.sleep(4)

conn.send(b"Halo dari server!")
conn.close()
server.close()
