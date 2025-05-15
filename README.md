# 📨 P2P Chat Application

A peer-to-peer (P2P) chat system built in Python that allows users to discover each other over a Local Area Network (LAN) and communicate in real-time via secure and unsecure TCP messaging.

---

## 📌 Features

- 🔍 Peer discovery over LAN using UDP broadcasts
- 💬 TCP chat communication (secure and unsecure)
- 🔐 AES-encrypted messaging using Diffie-Hellman key exchange
- 🕓 Real-time chat logging with timestamps
- ✅ Fully decentralized — no central server needed

---

## 📁 Project Structure

```
p2p_chat/
├── service_announcer.py        # Broadcasts your presence every 8 seconds
├── peer_discovery.py           # Listens for broadcasts, builds user list
├── chat_initiator.py           # Menu-driven chat starter
├── chat_responder.py           # Listens for incoming chat
├── utils.py or crypto_utils.py # Encryption, key generation helpers
├── shared_data.txt             # Stores discovered peers
├── chat_log.txt                # Stores message history
└── README.md
```

---

## ⚙️ How to Run on LAN (Multiple PCs)

🛜 **LAN Setup (e.g. Wi-Fi):**

1. Make sure all PCs are connected to **same Wi-Fi network**
2. Each user must run:
   - `service_announcer.py`
   - `peer_discovery.py`
   - `chat_responder.py`
3. One user runs `chat_initiator.py` to chat

---

## 🌐 IP & Port Setup (LAN)

| File | IP / Broadcast | Port |
|------|----------------|------|
| `service_announcer.py` | Use LAN broadcast IP like `192.168.1.255` | `7000` |
| `peer_discovery.py`    | Bind to `('', 7000)`                     | `7000` |
| `chat_responder.py`    | Bind to `('', 7001)`                     | `7001` |
| `chat_initiator.py`    | Uses IP from `shared_data.txt`           | `7001` |

📌 Get your PC’s IP using `ipconfig` (Windows) or `ifconfig` (Linux)  
Use **subnet broadcast address** based on your IP.

---

## 🧪 How to Test on Single PC (localhost)

You can simulate two users by running in multiple terminals:

1. Terminal 1: `python peer_discovery.py`
2. Terminal 2: `python service_announcer.py` (username: Ali)
3. Terminal 3: `python service_announcer.py` (username: Sara)
4. Terminal 4: `python chat_responder.py`
5. Terminal 5: `python chat_initiator.py` (Sara chats with Ali)

📌 Use IP: `127.0.0.1` in this case.

---

## 🔐 Secure Chat (Diffie-Hellman + AES)

- User chooses secure or unsecure mode
- For secure:
  - Diffie-Hellman key exchange (p=19, g=2)
  - Shared key is used for AES encryption
- Uses `pycryptodome` for AES ECB mode

---

## 🛠 Requirements

Install the required library:

```bash
pip install pycryptodome
```

Python 3.x must be installed.

---

## 🏁 Run Commands

```bash
# Run peer discovery listener
python peer_discovery.py

# Broadcast your username to network
python service_announcer.py

# Respond to messages
python chat_responder.py

# Initiate chat
python chat_initiator.py
```

---

## 📜 Chat History

All sent/received messages are stored in `chat_log.txt` as:

```
2025-05-15 10:21:03,Ali,SENT,Hello!
2025-05-15 10:21:06,127.0.0.1,RECEIVED,Hi Sara!
```

---

## 📌 Notes

- Use consistent ports across scripts
- Make sure Python is allowed through firewall
- Delete `shared_data.txt` if peer list gets outdated

---

🛡️ **Built for learning, testing and academic use.**
