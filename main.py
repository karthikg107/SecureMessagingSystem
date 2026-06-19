from encryption import (
    encrypt_message,
    decrypt_message
)

message = "Hello Karthik"

encrypted = encrypt_message(message)

print("Encrypted:")
print(encrypted)

print()

decrypted = decrypt_message(encrypted)

print("Decrypted:")
print(decrypted)