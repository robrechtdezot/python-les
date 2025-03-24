from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PyQt5.QtCore import QTimer
import time
import random

class CodingChallengeApp(QWidget):
    def __init__(self):
        super().__init__()

        # Setup UI
        self.setWindowTitle("Coding Challenge Automator")
        self.setGeometry(100, 100, 600, 400)
        
        self.layout = QVBoxLayout()
        self.challenge_label = QLabel("Choose a difficulty level (Easy/Medium/Hard):")
        self.layout.addWidget(self.challenge_label)
        
        self.difficulty_input = QTextEdit()
        self.difficulty_input.setPlaceholderText("Enter your difficulty choice here (Easy/Medium/Hard)")
        self.layout.addWidget(self.difficulty_input)

        self.challenge_text = QLabel("Challenge:")
        self.layout.addWidget(self.challenge_text)

        self.code_input = QTextEdit()
        self.code_input.setPlaceholderText("Write your solution here...")
        self.layout.addWidget(self.code_input)

        self.start_button = QPushButton("Start Challenge")
        self.start_button.clicked.connect(self.start_challenge)
        self.layout.addWidget(self.start_button)

        self.submit_button = QPushButton("Submit Solution")
        self.submit_button.clicked.connect(self.submit_solution)
        self.submit_button.setEnabled(False)
        self.layout.addWidget(self.submit_button)

        self.timer_label = QLabel("Time: 0.00 seconds")
        self.layout.addWidget(self.timer_label)

        self.setLayout(self.layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.start_time = None
        self.elapsed_time = 0

    def start_challenge(self):
        difficulty = self.difficulty_input.toPlainText().strip()
        if difficulty not in ["Easy", "Medium", "Hard"]:
            self.challenge_label.setText("Invalid difficulty, try again.")
            return

        challenges = {
            "Easy": [
                "Write a function that reverses a string.",
                "Find the largest number in a list."
            ],
            "Medium": [
                "Implement a basic calculator that takes input as a string (e.g., '3 + 4 * 2').",
                "Find the longest word in a sentence."
            ],
            "Hard": [
                "Implement a simple encryption and decryption function using Caesar Cipher.",
                "Write a function that solves Sudoku puzzles."
            ]
        }

        self.current_challenge = random.choice(challenges[difficulty])
        self.challenge_text.setText(f"Challenge: {self.current_challenge}")
        
        self.elapsed_time = 0
        self.timer.start(1000)
        self.start_time = time.time()

        self.submit_button.setEnabled(True)

    def submit_solution(self):
        self.timer.stop()
        end_time = time.time()
        elapsed_time = end_time - self.start_time

        self.timer_label.setText(f"Time: {elapsed_time:.2f} seconds")
        self.save_best_time(elapsed_time)

    def update_timer(self):
        if self.start_time:
            self.elapsed_time = time.time() - self.start_time
            self.timer_label.setText(f"Time: {self.elapsed_time:.2f} seconds")

    def save_best_time(self, elapsed_time):
        try:
            with open('best_times.txt', 'a') as f:
                f.write(f"Challenge: {self.current_challenge} | Time: {elapsed_time:.2f} seconds\n")
            print(f"Best time saved: {elapsed_time:.2f} seconds")
        except Exception as e:
            print(f"Error saving best time: {e}")

app = QApplication([])
window = CodingChallengeApp()
window.show()
app.exec_()
