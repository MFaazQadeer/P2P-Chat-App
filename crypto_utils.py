from Crypto.Cipher import AES
import hashlib
import base64
import random

# --- Diffie-Hellman ---
p = 19  # Prime
g = 2   # Generator

def generate_dh_key():
    secret = random.randint(1, 10)
    public = (g ** secret) % p
    return public, secret

def compute_shared_key(their_key, my_secret):
    shared = (their_key ** my_secret) % p
    return shared

# --- Encryption ---
def encrypt_message(plain_text, key):
    key_bytes = hashlib.sha256(str(key).encode()).digest()
    cipher = AES.new(key_bytes, AES.MODE_ECB)
    pad = 16 - len(plain_text) % 16
    plain_text += chr(pad) * pad
    encrypted = cipher.encrypt(plain_text.encode())
    return base64.b64encode(encrypted).decode()

def decrypt_message(enc_text, key):
    key_bytes = hashlib.sha256(str(key).encode()).digest()
    cipher = AES.new(key_bytes, AES.MODE_ECB)
    enc = base64.b64decode(enc_text)
    decrypted = cipher.decrypt(enc).decode()
    pad = ord(decrypted[-1])
    return decrypted[:-pad]
