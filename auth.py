import sqlite3
import bcrypt
from logger import log_event


def register_user(username, password):
    conn = sqlite3.connect("secure_messaging.db")
    cursor = conn.cursor()

    password_hash = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    try:
        cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, password_hash.decode())
        )

        conn.commit()

        print("User registered successfully")

        log_event(
            f"User {username} registered"
        )

        conn.close()
        return True

    except sqlite3.IntegrityError:
        print("Username already exists")

        log_event(
            f"Registration failed for {username}"
        )

        conn.close()
        return False


def login_user(username, password):
    conn = sqlite3.connect("secure_messaging.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password_hash FROM users WHERE username = ?",
        (username,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        stored_hash = result[0]

        if bcrypt.checkpw(
            password.encode(),
            stored_hash.encode()
        ):
            print("Login successful")

            log_event(
                f"User {username} logged in"
            )

            return True

    print("Invalid username or password")

    log_event(
        f"Failed login attempt for {username}"
    )

    return False