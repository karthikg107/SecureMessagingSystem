import tkinter as tk
from auth import register_user, login_user
from tkinter import messagebox

from encryption import encrypt_message, decrypt_message
from integrity import generate_hmac, verify_hmac
from attack import detect_replay_attack


root = tk.Tk()

def login():
    username = username_entry.get()
    password = password_entry.get()

    if login_user(username, password):
        login_frame.pack_forget()
        app_frame.pack(fill="both", expand=True)

        messagebox.showinfo(
            "Success",
            "Login Successful"
        )
    else:
        messagebox.showerror(
            "Error",
            "Invalid Username or Password"
        )


def register():
    username = username_entry.get()
    password = password_entry.get()

    if register_user(username, password):
        messagebox.showinfo(
            "Success",
            "User Registered Successfully"
        )
    else:
        messagebox.showerror(
            "Error",
            "Username Already Exists"
        )


root.title("Secure Messaging System")
root.geometry("900x800")

login_frame = tk.Frame(root)

login_frame.pack(pady=50)

tk.Label(
    login_frame,
    text="Login / Register",
    font=("Arial", 18, "bold")
).pack(pady=10)

tk.Label(
    login_frame,
    text="Username"
).pack()

username_entry = tk.Entry(
    login_frame,
    width=30
)

username_entry.pack(pady=5)

tk.Label(
    login_frame,
    text="Password"
).pack()

password_entry = tk.Entry(
    login_frame,
    width=30,
    show="*"
)

password_entry.pack(pady=5)

tk.Button(
    login_frame,
    text="Login",
    command=login
).pack(pady=5)

tk.Button(
    login_frame,
    text="Register",
    command=register
).pack(pady=5)

app_frame = tk.Frame(root)

def encrypt_text():
    message = message_entry.get()

    encrypted = encrypt_message(message)

    encrypted_output.delete("1.0", tk.END)

    encrypted_output.insert(
        tk.END,
        encrypted
    )

def decrypt_text():
    encrypted = encrypted_output.get("1.0", tk.END).strip()

    decrypted = decrypt_message(encrypted)

    decrypted_output.delete("1.0", tk.END)

    decrypted_output.insert(
        tk.END,
        decrypted
    )    

def verify_integrity():
    message = message_entry.get()

    message_hmac = generate_hmac(message)

    if verify_hmac(message, message_hmac):
        integrity_status.config(
            text="Integrity Verified"
        )
    else:
        integrity_status.config(
            text="Integrity Failed"
        )    

def replay_attack_test():
    message_id = "MSG001"

    if detect_replay_attack(message_id):
        replay_status.config(
            text="Replay Attack Detected"
        )
    else:
        replay_status.config(
            text="Message Accepted"
        )        


title = tk.Label(
    app_frame,
    text="Secure Messaging System",
    font=("Arial", 18, "bold")
)

title.pack(pady=10)

message_label = tk.Label(
    app_frame,
    text="Message"
)

message_label.pack()

message_entry = tk.Entry(
    app_frame,
    width=60
)

message_entry.pack(pady=5)

encrypt_button = tk.Button(
    app_frame,
    text="Encrypt",
    command=encrypt_text
)

encrypt_button.pack(pady=10)

encrypted_label = tk.Label(
    app_frame,
    text="Encrypted Message"
)

encrypted_label.pack()

encrypted_output = tk.Text(
    app_frame,
    height=5,
    width=70
)

encrypted_output.pack(pady=5)

decrypt_button = tk.Button(
    app_frame,
    text="Decrypt",
    command=decrypt_text
)

decrypt_button.pack(pady=10)

decrypted_label = tk.Label(
    app_frame,
    text="Decrypted Message"
)

decrypted_label.pack()

decrypted_output = tk.Text(
    app_frame,
    height=5,
    width=70
)

decrypted_output.pack(pady=5)

verify_button = tk.Button(
    app_frame,
    text="Verify Integrity",
    command=verify_integrity
)

verify_button.pack(pady=10)

integrity_status = tk.Label(
    app_frame,
    text="Status: Not Checked",
    font=("Arial", 12, "bold")
)

integrity_status.pack(pady=5)

replay_button = tk.Button(
    app_frame,
    text="Replay Attack Test",
    command=replay_attack_test
)

replay_button.pack(pady=10)

replay_status = tk.Label(
    app_frame,
    text="Not Tested",
    font=("Arial", 12, "bold")
)

replay_status.pack(pady=5)

root.mainloop()