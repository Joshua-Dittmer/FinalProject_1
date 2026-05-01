from __future__ import annotations
from typing import Dict, Tuple
import csv
from pathlib import Path

from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtGui import QColor, QPalette

from finalproject1gui import Ui_MainWindow


VOTES_FILE = Path("votes.csv")


class Logic(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.votes: Dict[str, str] = {}
        self.load_votes()

        # Connect button
        self.button_submit.clicked.connect(self.submit_vote)

        # Update tally on startup
        self.update_tally()

    # -----------------------------
    # FILE HANDLING
    # -----------------------------
    def load_votes(self):
        if not VOTES_FILE.exists():
            return

        try:
            with VOTES_FILE.open("r", encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) == 2:
                        user_id, candidate = row
                        self.votes[user_id] = candidate
        except:
            pass

    def save_vote(self, user_id: str, candidate: str):
        try:
            with VOTES_FILE.open("a", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([user_id, candidate])
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not save vote:\n{e}")

    # -----------------------------
    # VALIDATION
    # -----------------------------
    def validate_id(self, user_id: str) -> bool:
        if user_id == "":
            self.set_message("ID cannot be empty", "red")
            return False

        if len(user_id) < 3:
            self.set_message("ID must be at least 3 characters", "red")
            return False

        if " " in user_id:
            self.set_message("ID cannot contain spaces", "red")
            return False

        return True

    # -----------------------------
    # MESSAGE COLORING
    # -----------------------------
    def set_message(self, text: str, color: str):
        self.label_message.setText(text)
        palette = self.label_message.palette()
        palette.setColor(QPalette.ColorRole.WindowText, QColor(color))
        self.label_message.setPalette(palette)

    # -----------------------------
    # TALLY
    # -----------------------------
    def get_tally(self) -> Tuple[int, int, int]:
        john = sum(1 for c in self.votes.values() if c == "John")
        jane = sum(1 for c in self.votes.values() if c == "Jane")
        total = len(self.votes)
        return john, jane, total

    def update_tally(self):
        john, jane, total = self.get_tally()
        self.label_john.setText(f"John - {john}")
        self.label_jane.setText(f"Jane - {jane}")
        self.label_total.setText(f"Total - {total}")

    # -----------------------------
    # MAIN VOTE HANDLER
    # -----------------------------
    def submit_vote(self):
        user_id = self.id_input.text().strip()

        # Validate ID
        if not self.validate_id(user_id):
            return

        # Check candidate
        if self.radio_jane.isChecked():
            candidate = "Jane"
        elif self.radio_john.isChecked():
            candidate = "John"
        else:
            self.set_message("Select a candidate", "red")
            return

        # Duplicate check
        if user_id in self.votes:
            self.set_message("Already Voted", "red")
            return

        # Save vote
        self.votes[user_id] = candidate
        self.save_vote(user_id, candidate)

        # Success
        self.set_message(f"Voted {candidate}", "green")

        # Clear inputs
        self.id_input.clear()
        self.radio_jane.setChecked(False)
        self.radio_john.setChecked(False)

        # Update tally
        self.update_tally()
