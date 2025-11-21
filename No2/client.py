import socket
import threading

def terima_pesan(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg:
                print("\n" + msg)
        except:
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5050))

print("Terhubung ke server!")

threading.Thread(target=terima_pesan, args=(client,), daemon=True).start()

while True:
    pesan = input("")
    client.send(pesan.encode())
