import random
import time
from datetime import datetime
import ast
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QMessageBox
from PyQt5.QtCore import QTimer


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
        self.current_challenge = None

    def start_challenge(self):
        difficulty = self.difficulty_input.toPlainText().strip()
        if difficulty not in ["Easy", "Medium", "Hard"]:
            self.challenge_label.setText("Invalid difficulty, try again.")
            return

        challenges = self.load_challenges()

        self.current_challenge = random.choice(challenges[difficulty])
        self.challenge_text.setText(f"Challenge: {self.current_challenge['question']}")

        self.elapsed_time = 0
        self.timer.start(1000)
        self.start_time = time.time()

        self.submit_button.setEnabled(True)

    def load_challenges(self):
        challenges = {"Easy": [], "Medium": [], "Hard": []}
        try:
            with open('challenges.txt') as f:
                file_lines = f.readlines()
                current_difficulty = None
                for line in file_lines:
                    line = line.strip()
                    if line.startswith("#") or not line:
                        continue

                    if line in ["Easy", "Medium", "Hard"]:
                        current_difficulty = line
                    else:
                        challenge, answer = line.split(" | answer: ")
                        challenge_data = {
                            "question": challenge,
                            "answer": answer.strip().replace("lambda", "def")  # convert lambda to a proper function
                        }
                        challenges[current_difficulty].append(challenge_data)
        except Exception as e:
            print(f"Error loading challenges: {e}")
        return challenges

    def submit_solution(self):
        self.timer.stop()
        end_time = time.time()
        elapsed_time = end_time - self.start_time

        # Get user input
        user_code = self.code_input.toPlainText().strip()

        # Try validating the solution
        is_correct = self.validate_solution(user_code)

        # Show if correct or not
        if is_correct:
            self.show_message("Correct!", f"You completed the challenge in {elapsed_time:.2f} seconds!")
        else:
            self.show_message("Incorrect!", "The solution is incorrect. Try again.")

        self.timer_label.setText(f"Time: {elapsed_time:.2f} seconds")
        self.save_submission(elapsed_time, is_correct)

    def validate_solution(self, user_code):
        try:
            # Try executing the user's solution in a controlled environment
            user_answer = eval(user_code)
            correct_answer_func = eval(self.current_challenge["answer"])

            if user_answer == correct_answer_func("test input", 3):  # Adjust for each challenge
                return True
            else:
                return False
        except Exception as e:
            print(f"Error validating solution: {e}")
            return False

    def update_timer(self):
        if self.start_time:
            self.elapsed_time = time.time() - self.start_time
            self.timer_label.setText(f"Time: {self.elapsed_time:.2f} seconds")

    def show_message(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information if "Correct" in title else QMessageBox.Warning)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()

    def save_submission(self, elapsed_time, is_correct):
        submission_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = "Correct" if is_correct else "Incorrect"
        try:
            with open('submissions.txt', 'a') as f:
                f.write(f"Date: {submission_date} | Challenge: {self.current_challenge['question']} | Result: {result} | Time: {elapsed_time:.2f} seconds\n")
            print(f"Submission saved: {result} in {elapsed_time:.2f} seconds")
        except Exception as e:
            print(f"Error saving submission: {e}")


app = QApplication([])
window = CodingChallengeApp()
window.show()
app.exec_()
