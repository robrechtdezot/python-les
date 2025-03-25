import asyncio
import edge_tts
import pyperclip
import simpleaudio as sa
from pydub import AudioSegment
import io
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QSlider, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import keyboard  # Ensure keyboard module is imported
import threading
import time

VOICE = "en-US-GuyNeural"  # Change to any voice

class SpeechThread(QThread):
    """Thread to handle the speech task."""
    finished = pyqtSignal()

    def __init__(self, text, speed):
        super().__init__()
        self.text = text
        self.speed = speed

    async def speak_text(self):
        """Uses Edge TTS to generate and play audio instantly."""
        rate_value = f"+{self.speed}%" if self.speed >= 0 else f"{self.speed}%"
        tts = edge_tts.Communicate(self.text, VOICE, rate=rate_value)
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

        # Play the new audio
        wave_obj = sa.WaveObject.from_wave_file(wav_io)
        wave_obj.play()

        self.finished.emit()  # Emit finished signal when done

    def run(self):
        """Start the async task in the event loop."""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.speak_text())

class TextToSpeechApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.speed = 0  # Default speed (0%)
        self.speech_playing = False  # Flag to track if speech is playing
        self.exit_flag = False  # Flag to exit the program cleanly
        self.speech_task = None  # To track the async task for speech

        # Start hotkey listening in a background thread
        self.hotkey_thread = threading.Thread(target=self.run_hotkeys, daemon=True)
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

        # Stop button
        self.stop_button = QPushButton("Stop", self)
        self.stop_button.clicked.connect(self.stop_speech)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.speed_label)
        layout.addWidget(self.speed_slider)
        layout.addWidget(self.stop_button)
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

    def stop_speech(self):
        """Stops the speech if it's currently playing."""
        if self.speech_playing:
            print("Stopping speech...")
            self.speech_playing = False
            print("Speech stopped!")

    def read_selected_text(self):
        """Simulates reading the selected text aloud."""
        keyboard.press_and_release('ctrl+c')  # Simulate 'Copy' (Windows/Linux)
        time.sleep(0.5)  # Wait for clipboard to update
        text = pyperclip.paste()  # Get clipboard content
        if text:
            print("Reading:", text)
            self.speech_playing = True  # Mark that speech is starting
            self.speech_task = SpeechThread(text, self.speed)  # Create a new thread for speech
            self.speech_task.finished.connect(self.on_speech_finished)  # Connect finished signal
            self.speech_task.start()  # Start the thread
        else:
            print("No text selected!")

    def on_speech_finished(self):
        """Callback for when speech is finished."""
        self.speech_playing = False
        print("Speech finished.")

    def run_hotkeys(self):
        """Run hotkey listener in a separate thread"""
        while not self.exit_flag:
            if keyboard.is_pressed('F9'):  # Press F9 to read selected text
                if not self.speech_playing:  # Only start reading if no speech is playing
                    self.read_selected_text()
            time.sleep(0.1)  # Small delay to prevent overloading the CPU

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TextToSpeechApp()
    sys.exit(app.exec_())
