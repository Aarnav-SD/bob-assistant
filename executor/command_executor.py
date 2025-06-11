import os
from pathlib import Path
import subprocess
import pyautogui
import time
import webbrowser
from executor.app_mapper import resolve_app

def normalize_action_name(action):
    if not action:
        return None
    return action.strip().lower().replace(" ", "_")

def execute_command_json(commands):
    if not isinstance(commands, list):
        commands = [commands]

    for cmd in commands:
        action = normalize_action_name(cmd.get("action"))
        cmd["action"] = action  

        if action == "open_app":
            open_app(cmd.get("target") or cmd.get("application"))

        elif action == "write_text":
            write_text(cmd.get("text"))

        elif action == "search_browser":
            query = cmd.get("query") or cmd.get("text") or cmd.get("target")
            if query:
                webbrowser.open(f"https://www.google.com/search?q={query}")

        elif action == "open_browser":
            target = cmd.get("url") or cmd.get("target")
            if target:
                if not target.startswith("http"):
                    if "." not in target:
                        target += ".com"
                    target = f"https://{target}"
                webbrowser.open(target)

        elif action == "adjust_volume":
            adjust_volume(cmd.get("level"))

        elif action == "run_os_command":
            run_os_command(cmd.get("command") or cmd.get("text"))

        elif action == "control_spotify":
            control_spotify(cmd.get("command"))
        
        elif action == "create_folder":
            create_project_folder(
                name=cmd.get("folder_name"),
                location=cmd.get("location"),
            )

        else:
            print(f"Unknown action: {action}")

def open_app(app_name):
    try:
        executable = resolve_app(app_name)
        subprocess.Popen(executable)
    except Exception as e:
        print(f"Failed to open app: {app_name}. Error: {str(e)}")

def write_text(text):
    time.sleep(2)  
    pyautogui.write(text or "")

def adjust_volume(level):
    if level == "up":
        pyautogui.press("volumeup")
    elif level == "down":
        pyautogui.press("volumedown")
    elif level == "mute":
        pyautogui.press("volumemute")

def run_os_command(command):
    try:
        subprocess.Popen(command, shell=True)
    except Exception as e:
        print(f"Failed to execute OS command: {str(e)}")

def control_spotify(command):
    command = command.lower() if command else ""
    if command in ["play", "resume", "start"]:
        pyautogui.press("playpause")
    elif command == "pause":
        pyautogui.press("playpause")
    elif command == "next":
        pyautogui.press("nexttrack")
    elif command == "previous" or command == "prev":
        pyautogui.press("prevtrack")
    else:
        print(f"Unsupported Spotify command: {command}")


def create_project_folder(name, location="desktop"):
    user_dir = Path.home()
    cd = Path.cwd()

    base_dirs = {
        "desktop": user_dir / "Desktop",
        "documents": user_dir / "Documents",
        "downloads": user_dir / "Downloads",
        "here": cd
    }

    base_path = base_dirs.get(location.lower(), user_dir)
    folder_path = base_path / name

    try:
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_path}")

    except Exception as e:
        print(f"Failed to create project folder: {e}")