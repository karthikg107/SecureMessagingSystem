from attack import detect_replay_attack

message_id = "MSG001"

if detect_replay_attack(message_id):
    print("Replay Attack Detected")
else:
    print("Message Accepted")

if detect_replay_attack(message_id):
    print("Replay Attack Detected")
else:
    print("Message Accepted")