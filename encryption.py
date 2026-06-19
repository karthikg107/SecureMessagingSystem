from cryptography.fernet import Fernet
from key_manager import load_key
from logger import log_event

key = load_key()

cipher = Fernet(key)

def encrypt_message(message):
    encrypted = cipher.encrypt(message.encode()

    )
    log_event("Message encrypted")

    return encrypted.decode()

def decrypt_message(encrypted_message):
    decrypted = cipher.decrypt(
        encrypted_message.encode()
    )

    log_event("Message decrypted")

    return decrypted.decode()