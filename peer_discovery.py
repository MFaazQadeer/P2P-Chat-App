import socket
import json
import time

PORT = 7000
BUFFER_SIZE = 1024
DATA_FILE = 'shared_data.txt'

# Dictionary to store peers: ip -> (username, last_seen_time)
peers = {}

# Start UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', PORT))  # '' means listen on all interfaces

print(f"[LISTENING] Peer Discovery is listening on UDP port {PORT}...\n")

def save_peers_to_file():
    with open(DATA_FILE, 'w') as f:
        for username, (ip, last_seen) in peers.items():
            f.write(f"{ip},{username},{last_seen}\n")

        # for ip, (username, last_seen) in peers.items():
        #     f.write(f"{ip},{username},{last_seen}\n")

while True:
    try:
        data, addr = sock.recvfrom(BUFFER_SIZE)
        ip = addr[0]
        message = json.loads(data.decode('utf-8'))

        username = message.get("username")
        timestamp = time.time()

        if ip in peers:
            peers[username] = (ip, timestamp)

            # peers[ip] = (username, timestamp)  # Update time
            print(f"[UPDATE] {username} ({ip}) is still online.")
        else:
            peers[ip] = (username, timestamp)  # New user
            print(f"[NEW] {username} ({ip}) joined the network.")

        save_peers_to_file()

    except Exception as e:
        print(f"[ERROR] {e}")
