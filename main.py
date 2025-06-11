from tkinter import Tk
from gui.bob_gui import BobGUI
from core.parser import parse_command_with_bob
from executor.command_executor import execute_command_json

def handle_text_command(command):
    gui.update_status("Thinking...")
    response = parse_command_with_bob(command)

    try:
        parsed = eval(response.strip())
        execute_command_json(parsed)
        gui.display_message("Bob", f"Executing: {parsed}")
    except:
        gui.display_message("Bob", response)

    gui.update_status("Idle")

if __name__ == "__main__":
    root = Tk()
    gui = BobGUI(root, on_submit_callback=handle_text_command)
    root.mainloop()
