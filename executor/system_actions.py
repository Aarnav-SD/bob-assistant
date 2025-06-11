
import pyautogui

def adjust_volume(level):
    if level == "up":
        pyautogui.press("volumeup")
    elif level == "down":
        pyautogui.press("volumedown")
    elif level == "mute":
        pyautogui.press("volumemute")
