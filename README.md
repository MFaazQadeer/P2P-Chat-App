# 📨 P2P Chat Application (Python)

A peer-to-peer (P2P) chat application for Local Area Networks (LAN), supporting secure and unsecure messaging using TCP sockets and Diffie-Hellman encryption.

## 📌 Features

- Peer discovery using UDP broadcasting
- Secure chat using AES encryption + Diffie-Hellman key exchange
- Unsecure chat over TCP
- Chat history logging
- Works on same system (127.0.0.1) for testing
- Fully built using Python sockets

## 📁 Project Structure

p2p_chat/
├── service_announcer.py
├── peer_discovery.py
├── chat_initiator.py
├── chat_responder.py
├── utils.py / crypto_utils.py
├── shared_data.txt
├── chat_log.txt
└── README.md


## 🚀 How to Run

Open 4 terminals and run:

1. `python peer_discovery.py`
2. `python chat_responder.py`
3. `python service_announcer.py` (User 1)
4. `python chat_initiator.py` (User 2)

## 🔐 Secure Chat

- Uses Diffie-Hellman key exchange (p=19, g=2)
- Encrypts messages with AES ECB mode
