import socket
import json
import time

# Ask user to enter their username
username = input("Enter your username: ")

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Windows sometimes blocks broadcasts — make sure firewall allows Python
broadcast_ip = '127.0.0.255'  # LAN broadcast
port = 7000

while True:
    message = json.dumps({"username": username})
    sock.sendto(message.encode('utf-8'), (broadcast_ip, port))
    print(f"[INFO] Broadcast sent: {message}")
    time.sleep(8)
