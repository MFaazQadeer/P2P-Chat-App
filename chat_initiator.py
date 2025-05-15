import socket
import json
import time
from crypto_utils import encrypt_message, generate_dh_key, compute_shared_key

PORT = 7001
DATA_FILE = 'shared_data.txt'
LOG_FILE = 'chat_log.txt'

def load_peers():
    peers = {}
    try:
        with open(DATA_FILE, 'r') as f:
            for line in f:
                ip, username, last_seen = line.strip().split(',')
                last_seen = float(last_seen)
                peers[username] = (ip, last_seen)
    except:
        pass
    return peers

def show_users():
    peers = load_peers()
    print("\n🧑 Online Users:")
    for name, (ip, last_seen) in peers.items():
        seconds_ago = time.time() - last_seen
        status = "Online" if seconds_ago <= 10 else "Away"
        print(f"- {name} ({status})")
    print()

def show_history():
    print("\n Chat History:")
    try:
        with open(LOG_FILE, 'r') as f:
            for line in f:
                print(line.strip())
    except:
        print("No history found.")
    print()

def start_chat():
    peers = load_peers()
    usernames = list(peers.keys())

    if not usernames:
        print(" No users available to chat.")
        return

    print("\nWho do you want to chat with?")
    for i, user in enumerate(usernames):
        print(f"{i + 1}. {user}")
    
    choice = int(input("Enter number: ")) - 1
    if choice < 0 or choice >= len(usernames):
        print("Invalid choice.")
        return

    target_user = usernames[choice]
    ip = peers[target_user][0]

    secure = input("Secure chat? (y/n): ").lower() == 'y'
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, PORT))

        if secure:
            my_key, my_secret = generate_dh_key()
            sock.send(json.dumps({"key": my_key}).encode('utf-8'))

            their_key_json = sock.recv(1024)
            their_key = json.loads(their_key_json.decode('utf-8'))["key"]
            shared_key = compute_shared_key(their_key, my_secret)

            msg = input("Type your message: ")
            encrypted_msg = encrypt_message(msg, shared_key)
            message = json.dumps({"encrypted message": encrypted_msg})

        else:
            msg = input("Type your message: ")
            message = json.dumps({"unencrypted message": msg})

        sock.send(message.encode('utf-8'))
        sock.close()

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with open(LOG_FILE, 'a') as f:
            f.write(f"{timestamp},{target_user},SENT,{msg}\n")

        print("[✅] Message sent.")

    except Exception as e:
        print(f"[❌] Failed to send message: {e}")

def main():
    while True:
        print("\n===== Chat Menu =====")
        print("1. View Users")
        print("2. Chat")
        print("3. History")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == '1':
            show_users()
        elif choice == '2':
            start_chat()
        elif choice == '3':
            show_history()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
