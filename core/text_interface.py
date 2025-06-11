
from core.parser import parse_command_with_bob
from executor.command_executor import execute_command_json

def run_cli_interface():
    print("Bob (Text Mode): Type your commands below. Type '/exit' to quit.")
    while True:
        command = input("You: ").strip()
        if command.lower() in ["/exit", "exit", "quit"]:
            print("Bob: Goodbye!")
            break

        response = parse_command_with_bob(command)
        print(f"Bob: {response}")

        try:
            parsed = eval(response.strip())
            execute_command_json(parsed)
        except:
            pass