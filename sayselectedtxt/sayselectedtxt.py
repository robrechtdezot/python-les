import pyttsx3
import pyperclip
import keyboard
import time

def speak_text(text):
    """Speaks the given text."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def read_selected_text():
    """Simulates copy and reads the selected text aloud."""
    keyboard.press_and_release('ctrl+c')  # Simulate 'Copy' (Windows/Linux)
    time.sleep(0.5)  # Wait for clipboard to update

    text = pyperclip.paste()  # Get clipboard content
    if text:
        print("Reading:", text)
        speak_text(text)
    else:
        print("No text selected!")

# Set a global hotkey (e.g., F9)
keyboard.add_hotkey("F9", read_selected_text)

print("Press F9 to read selected text aloud.")
keyboard.wait()  # Keep the script running
