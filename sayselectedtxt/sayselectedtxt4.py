import asyncio
import edge_tts
import pyperclip
import time
import simpleaudio as sa
from pydub import AudioSegment
import io
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QSlider, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
import threading
import keyboard

VOICE = "en-US-JennyNeural"  # Change to any voice

class TextToSpeechApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.speed = 0  # Default speed (0%)
        self.exit_flag = False  # Flag to control the exit
        self.hotkey_thread = threading.Thread(target=self.run_hotkeys)
        self.hotkey_thread.daemon = True
        self.hotkey_thread.start()

    def init_ui(self):
        self.setWindowTitle('Text to Speech')
        
        # Speed control
        self.speed_label = QLabel("Speed Control", self)
        self.speed_slider = QSlider(Qt.Horizontal, self)
        self.speed_slider.setMinimum(-50)  # Minimum speed (-50%)
        self.speed_slider.setMaximum(100)  # Maximum speed (+100%)
        self.speed_slider.setValue(0)  # Default speed (0%)
        self.speed_slider.setTickInterval(10)
        self.speed_slider.setTickPosition(QSlider.TicksBelow)
        self.speed_slider.valueChanged.connect(self.update_speed_label)

        # Exit button
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.clicked.connect(self.close_application)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.speed_label)
        layout.addWidget(self.speed_slider)
        layout.addWidget(self.exit_button)

        self.setLayout(layout)
        self.show()

    def update_speed_label(self):
        """Update the label with the current speed value"""
        self.speed = self.speed_slider.value()
        self.speed_label.setText(f"Speed: {self.speed}%")

    def close_application(self):
        """Close the application"""
        print("Exiting...")
        self.exit_flag = True
        self.close()

    async def speak_text(self, text):
        """Uses Edge TTS to generate and play audio instantly."""
        # Ensure the speed value is formatted correctly for Edge TTS
        rate_value = f"+{self.speed}%" if self.speed >= 0 else f"{self.speed}%"
        tts = edge_tts.Communicate(text, VOICE, rate=rate_value)
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

    def read_selected_text(self):
        """Simulates reading the selected text aloud."""
             
        keyboard.press_and_release('ctrl+c')  # Simulate 'Copy' (Windows/Linux)
        time.sleep(0.5)  # Wait for clipboard to update

        text = pyperclip.paste()   # Get clipboard content
        if text:
            print("Reading:", text)
            asyncio.run(self.speak_text(text))  # Use async for Edge TTS
        else:
            print("No text selected!")

    def run_hotkeys(self):
        """Run hotkey listener in a separate thread"""
        keyboard.add_hotkey('F9', self.read_selected_text)  # Press F9 to read selected text
        keyboard.add_hotkey('F10', self.close_application)  # Press F10 to exit
        keyboard.wait()  # Keeps the program listening for hotkeys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TextToSpeechApp()
    sys.exit(app.exec_())
