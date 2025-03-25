import asyncio
import edge_tts
import pyperclip
import keyboard
import time
import simpleaudio as sa
from pydub import AudioSegment
import io
import threading

VOICE = "en-US-JennyNeural"  # Change to any voice
SPEED = "+50%"  # Adjust speed (-50% to +100%)
exit_flag = False

async def speak_text(text):
    """Uses Edge TTS to generate and play audio instantly."""
    tts = edge_tts.Communicate(text, VOICE, rate=SPEED)
    buffer = io.BytesIO()

    async for chunk in tts.stream():
        if chunk["type"] == "audio":
            buffer.write(chunk["data"])
    
    buffer.seek(0)
    
    # Convert MP3 to WAV (required for simpleaudio)
    audio = AudioSegment.from_file(buffer, format="mp3")
    wav_io = io.BytesIO()
    audio.export(wav_io, format="wav")
    wav_io.seek(0)

    # Play the audio instantly
    wave_obj = sa.WaveObject.from_wave_file(wav_io)
    play_obj = wave_obj.play()
    play_obj.wait_done()

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

def exit_program():
    """Set the exit flag to True to stop the program."""
    global exit_flag
    print("Exiting...")
    exit_flag = True
# Set hotkeys
keyboard.add_hotkey("F9", read_selected_text)  # Read selected text
keyboard.add_hotkey("F10", exit_program)  # Exit script

print("Press F9 to read selected text aloud with a natural voice.")
print("Press F10 to exit.")

# Run the hotkey listener in a separate thread to handle it in the background
hotkey_thread = threading.Thread(target=keyboard.wait)
hotkey_thread.daemon = True  # Ensure the thread exits when the program does
hotkey_thread.start()

# Keep the main program running while the hotkeys are active
while not exit_flag:
    time.sleep(0.1) # Keep the script running

print("Program has exited.")