

def choose_input_mode():
    mode = input("Choose input mode (voice/text): ").strip().lower()
    return mode if mode in ["voice", "text"] else "text"