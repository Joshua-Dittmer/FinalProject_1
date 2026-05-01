from PyQt6.QtWidgets import QApplication
import sys
from finalproject1logic import Logic

def main():
    app = QApplication(sys.argv)
    window = Logic()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
