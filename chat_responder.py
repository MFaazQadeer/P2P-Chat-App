import socket
import json
import time
from crypto_utils import decrypt_message, generate_dh_key, compute_shared_key

PORT = 7001
BUFFER_SIZE = 1024
chat_log_file = 'chat_log.txt'
shared_keys = {}

# TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', PORT))
sock.listen(5)

print(f"[LISTENING] Chat Responder is listening on TCP port {PORT}...\n")

while True:
    try:
        conn, addr = sock.accept()
        data = conn.recv(BUFFER_SIZE)
        ip = addr[0]

        message = json.loads(data.decode('utf-8'))
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # CASE 1: Key Exchange
        if "key" in message:
            client_key = int(message["key"])
            my_key, my_secret = generate_dh_key()
            conn.send(json.dumps({"key": my_key}).encode('utf-8'))

            shared_keys[ip] = compute_shared_key(client_key, my_secret)
            print(f"[KEY] Shared key established with {ip}")

        # CASE 2: Encrypted Message
        elif "encrypted message" in message:
            encrypted_text = message["encrypted message"]
            if ip in shared_keys:
                key = shared_keys[ip]
                plain = decrypt_message(encrypted_text, key)
                print(f"[SECURE] {ip}: {plain}")
                with open(chat_log_file, 'a') as f:
                    f.write(f"{timestamp},{ip},RECEIVED,{plain}\n")
            else:
                print(f"[ERROR] No shared key for {ip}")

        # CASE 3: Unencrypted Message
        elif "unencrypted message" in message:
            plain = message["unencrypted message"]
            print(f"[CHAT] {ip}: {plain}")
            with open(chat_log_file, 'a') as f:
                f.write(f"{timestamp},{ip},RECEIVED,{plain}\n")

        conn.close()

    except Exception as e:
        print(f"[ERROR] {e}")
