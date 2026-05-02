import sys
from PyQt6.QtWidgets import QApplication
from logic import Logic
 
 
def main() -> None:
    """Launch the Bank Account Manager application."""
    application = QApplication(sys.argv)
    window = Logic()
    window.show()
    application.exec()
 
 
if __name__ == '__main__':
    main()
 