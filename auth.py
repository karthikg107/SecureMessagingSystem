import sqlite3
import bcrypt


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

    except sqlite3.IntegrityError:
        print("Username already exists")

    conn.close()