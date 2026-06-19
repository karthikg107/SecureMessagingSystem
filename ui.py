import tkinter as tk
from encryption import encrypt_message, decrypt_message
from integrity import generate_hmac, verify_hmac
from attack import detect_replay_attack


root = tk.Tk()


root.title("Secure Messaging System")
root.geometry("900x800")


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
    root,
    text="Secure Messaging System",
    font=("Arial", 18, "bold")
)

title.pack(pady=10)

message_label = tk.Label(
    root,
    text="Message"
)

message_label.pack()

message_entry = tk.Entry(
    root,
    width=60
)

message_entry.pack(pady=5)

encrypt_button = tk.Button(
    root,
    text="Encrypt",
    command=encrypt_text
)

encrypt_button.pack(pady=10)

encrypted_label = tk.Label(
    root,
    text="Encrypted Message"
)

encrypted_label.pack()

encrypted_output = tk.Text(
    root,
    height=5,
    width=70
)

encrypted_output.pack(pady=5)

decrypt_button = tk.Button(
    root,
    text="Decrypt",
    command=decrypt_text
)

decrypt_button.pack(pady=10)

decrypted_label = tk.Label(
    root,
    text="Decrypted Message"
)

decrypted_label.pack()

decrypted_output = tk.Text(
    root,
    height=5,
    width=70
)

decrypted_output.pack(pady=5)

verify_button = tk.Button(
    root,
    text="Verify Integrity",
    command=verify_integrity
)

verify_button.pack(pady=10)

integrity_status = tk.Label(
    root,
    text="Status: Not Checked",
    font=("Arial", 12, "bold")
)

integrity_status.pack(pady=5)

replay_button = tk.Button(
    root,
    text="Replay Attack Test",
    command=replay_attack_test
)

replay_button.pack(pady=10)

replay_status = tk.Label(
    root,
    text="Not Tested",
    font=("Arial", 12, "bold")
)

replay_status.pack(pady=5)

root.mainloop()