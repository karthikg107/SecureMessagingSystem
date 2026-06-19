processed_messages = set()


def detect_replay_attack(message_id):
    if message_id in processed_messages:
        return True

    processed_messages.add(message_id)
    return False