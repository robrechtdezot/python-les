import asyncio
import edge_tts
import pyperclip
import keyboard
import time
import os

VOICE = "en-US-JennyNeural"  # Change voice here (e.g., "en-GB-SoniaNeural")

async def speak_text(text):
    """Uses Edge TTS to read text aloud."""
    filename = "temp_audio.mp3"
    tts = edge_tts.Communicate(text, VOICE)
    await tts.save(filename)
    os.system(f"start {filename}" if os.name == "nt" else f"mpg123 {filename}")

def read_selected_text():
    """Simulates copy and reads the selected text aloud."""
    keyboard.press_and_release('ctrl+c')  # Simulate 'Copy' (Windows/Linux)
    time.sleep(0.5)  # Wait for clipboard to update

    text = pyperclip.paste()  # Get clipboard content
    if text:
        print("Reading:", text)
        asyncio.run(speak_text(text))  # Use async for Edge TTS
    else:
        print("No text selected!")

# Set a global hotkey (e.g., F9)
keyboard.add_hotkey("F9", read_selected_text)

print("Press F9 to read selected text aloud with a natural voice.")
keyboard.wait()  # Keep the script running
