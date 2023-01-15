import Controller
from PyQt6.QtWidgets import QApplication
import sys

def main():
    app = QApplication(sys.argv)
    ex = Controller.Controller()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()