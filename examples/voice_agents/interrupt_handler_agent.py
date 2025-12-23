IGNORE_WORDS = {"yeah", "ok", "hmm", "uh-huh", "right" ,'aha'}
INTERRUPT_WORDS = {"stop", "wait", "no"}

def classify_user_input(text: str, agent_is_speaking: bool) -> str:
    text = text.lower().strip()
    tokens = text.split()

    if agent_is_speaking:
        if any(word in text for word in INTERRUPT_WORDS):
            return "INTERRUPT"
        if tokens and all(token in IGNORE_WORDS for token in tokens):
            return "IGNORE"
        return "INTERRUPT"
    else:
        return "RESPOND"
