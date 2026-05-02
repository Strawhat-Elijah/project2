import sys
from PyQt6.QtWidgets import QApplication
from logic import BankController

def main() -> None:
    """Launch the Bank Account Manager application."""
    app = QApplication(sys.argv)
    controller = BankController()
    controller.show()
    sys.exit(app.exec())
 
 
if __name__ == "__main__":
    main()