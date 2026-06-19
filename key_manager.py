from cryptography.fernet import Fernet
import os


KEY_FILE = "secret.key"


def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()

        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)

        return key

    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()