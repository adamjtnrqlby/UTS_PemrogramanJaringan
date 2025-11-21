import socket
import threading

clients = []

def handle_client(conn, addr):
    print(f"[TERHUBUNG] {addr}")
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break
            print(f"[{addr}] {msg}")
            broadcast(f"{addr}: {msg}", conn)
        except:
            break

    clients.remove(conn)
    conn.close()
    print(f"[PUTUS] {addr}")

def broadcast(message, sender_conn):
    for client in clients:
        if client != sender_conn:
            try:
                client.send(message.encode())
            except:
                pass

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5050))
    server.listen()

    print("[SERVER JALAN] Menunggu client...")

    while True:
        conn, addr = server.accept()
        clients.append(conn)
        threading.Thread(target=handle_client, args=(conn, addr)).start()

start_server()
