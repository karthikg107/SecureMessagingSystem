from cryptography.fernet import Fernet

key = Fernet.generate_key()

cipher = Fernet(key)

def encrypt_message(message):
    encrypted = cipher.encrypt(message.encode())
    return encrypted.decode()

def decrypt_message(encrypted_message):
    decrypted = cipher.decrypt(encrypted_message.encode())
    return decrypted.decode()