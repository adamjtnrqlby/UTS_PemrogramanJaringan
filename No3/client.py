import socket

HOST = "127.0.0.1"
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Timeout CONNECT 3 detik
client.settimeout(3)

try:
    client.connect((HOST, PORT))
    print("Terhubung ke server.")
except socket.timeout:
    print("Koneksi timeout! (saat connect)")
    exit()
except Exception as e:
    print("Gagal connect:", e)
    exit()

# Timeout RECEIVE 2 detik
client.settimeout(2)

try:
    data = client.recv(1024).decode()
    print("Dari server:", data)
except socket.timeout:
    print("Koneksi timeout! (saat menerima data)")
except Exception as e:
    print("Error:", e)

client.close()
