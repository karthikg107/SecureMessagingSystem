import hmac
import hashlib
from logger import log_event

SECRET_KEY = b"secure_key"


def generate_hmac(message):
    return hmac.new(
        SECRET_KEY,
        message.encode(),
        hashlib.sha256
    ).hexdigest()


def verify_hmac(message, received_hmac):
    calculated_hmac = generate_hmac(message)

    result = hmac.compare_digest(
        calculated_hmac,
        received_hmac
    )

    if result:
        log_event("Integrity verified")
    else:
        log_event("Integrity verification failed")

    return result