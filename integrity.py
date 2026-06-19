import hmac
import hashlib

SECRET_KEY = b"secure_key"


def generate_hmac(message):
    return hmac.new(
        SECRET_KEY,
        message.encode(),
        hashlib.sha256
    ).hexdigest()


def verify_hmac(message, received_hmac):
    calculated_hmac = generate_hmac(message)

    return hmac.compare_digest(
        calculated_hmac,
        received_hmac
    )