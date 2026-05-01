from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QRadioButton, QPushButton,
    QVBoxLayout, QHBoxLayout, QGroupBox
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QWidget):
        MainWindow.setWindowTitle("Voting Application")
        MainWindow.resize(450, 320)

        self.layout = QVBoxLayout(MainWindow)

        # Title
        self.title_label = QLabel("VOTING APPLICATION")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.title_label)

        # ID row
        id_layout = QHBoxLayout()
        self.id_label = QLabel("ID:")
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("Enter unique ID")
        id_layout.addWidget(self.id_label)
        id_layout.addWidget(self.id_input)
        self.layout.addLayout(id_layout)

        # Candidate group
        self.candidate_groupbox = QGroupBox("Candidates")
        candidate_layout = QHBoxLayout()

        self.radio_jane = QRadioButton("Jane")
        self.radio_john = QRadioButton("John")

        candidate_layout.addWidget(self.radio_jane)
        candidate_layout.addWidget(self.radio_john)

        self.candidate_groupbox.setLayout(candidate_layout)
        self.layout.addWidget(self.candidate_groupbox)

        # Submit button
        self.button_submit = QPushButton("SUBMIT VOTE")
        self.layout.addWidget(self.button_submit)

        # Message label
        self.label_message = QLabel("")
        self.label_message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.label_message)

        # Tally group
        self.tally_groupbox = QGroupBox("Current Tally")
        tally_layout = QVBoxLayout()

        self.label_john = QLabel("John - 0")
        self.label_jane = QLabel("Jane - 0")
        self.label_total = QLabel("Total - 0")

        for lbl in (self.label_john, self.label_jane, self.label_total):
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            tally_layout.addWidget(lbl)

        self.tally_groupbox.setLayout(tally_layout)
        self.layout.addWidget(self.tally_groupbox)
