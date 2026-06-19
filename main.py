from integrity import (
    generate_hmac,
    verify_hmac
)

original_message = "Hello Karthik"

message_hmac = generate_hmac(original_message)

print("Original HMAC:")
print(message_hmac)

print()

tampered_message = "Hello Hacker"

if verify_hmac(tampered_message, message_hmac):
    print("Integrity Verified")
else:
    print("Integrity Failed")