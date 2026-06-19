from logger import log_event

processed_messages = set()


def detect_replay_attack(message_id):
    if message_id in processed_messages:
        log_event("Replay attack detected")
        return True

    processed_messages.add(message_id)

    log_event("Message accepted")

    return False