import requests
from config import OLLAMA_URL, OLLAMA_MODEL

def parse_command_with_bob(user_input):
    prompt = f"""
You are Bob, a hybrid assistant. Your job is to:
1. Understand whether the user is giving an OS command or just chatting.
2. If the input is an OS command (like opening apps, typing text, searching online, controlling system volume, etc.), output a JSON object describing the actions.
3. If the input is general conversation or a question, respond naturally like a helpful assistant.

COMMAND: {user_input}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code == 200:
        return response.json().get("response", "No response received from Bob.")
    else:
        return f"Error from Bob: {response.status_code}"