from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import (
    QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView
)


class Ui_MainWindow(object):
    """Generated UI class from QT Designer."""

    def setupUi(self, MainWindow: QMainWindow) -> None:
        """Set up the UI components on the main window."""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)

        self.title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.name_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.name_input.setObjectName("name_input")
        self.horizontalLayout.addWidget(self.name_input)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.account_type = QtWidgets.QComboBox(parent=self.centralwidget)
        self.account_type.setObjectName("account_type")
        self.account_type.addItem("Checking Account")
        self.account_type.addItem("Savings Account")
        self.horizontalLayout_2.addWidget(self.account_type)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.create_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.create_button.setObjectName("create_button")
        self.verticalLayout.addWidget(self.create_button)

        self.status_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.status_label.setObjectName("status_label")
        self.verticalLayout.addWidget(self.status_label)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.amount_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.amount_input.setObjectName("amount_input")
        self.horizontalLayout_3.addWidget(self.amount_input)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.deposit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.deposit_button.setObjectName("deposit_button")
        self.horizontalLayout_4.addWidget(self.deposit_button)
        self.withdraw_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.withdraw_button.setObjectName("withdraw_button")
        self.horizontalLayout_4.addWidget(self.withdraw_button)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.balance_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.balance_label.setObjectName("balance_label")
        self.verticalLayout.addWidget(self.balance_label)

        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)

        self.history_table = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.history_table.setObjectName("history_table")
        self.history_table.setColumnCount(3)
        self.history_table.setRowCount(0)
        self.verticalLayout.addWidget(self.history_table)

        self.save_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.save_button.setObjectName("save_button")
        self.verticalLayout.addWidget(self.save_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow: QMainWindow) -> None:
        """Set the text for all UI components."""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bank Account Manager"))
        self.title_label.setText(_translate("MainWindow", "Bank Account Manager"))
        self.label.setText(_translate("MainWindow", "Account Name:"))
        self.label_2.setText(_translate("MainWindow", "Account Type:"))
        self.create_button.setText(_translate("MainWindow", "Create Account"))
        self.status_label.setText(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", "Amount ($):"))
        self.deposit_button.setText(_translate("MainWindow", "Deposit"))
        self.withdraw_button.setText(_translate("MainWindow", "Withdraw"))
        self.balance_label.setText(_translate("MainWindow", "Balance: —"))
        self.label_4.setText(_translate("MainWindow", "Transaction History:"))
        self.save_button.setText(_translate("MainWindow", "Save to CSV"))


class BankAppWindow(QMainWindow, Ui_MainWindow):
    """Main application window for the Bank Account Manager."""

    def __init__(self) -> None:
        """Initialize the window and set up the UI."""
        super().__init__()
        self.setupUi(self)
        self.history_table.setHorizontalHeaderLabels(
            ["Account", "Transaction", "Balance After"]
        )
        self.history_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

    def get_name(self) -> str:
        """Return the account name input text."""
        return self.name_input.text().strip()

    def get_account_type(self) -> str:
        """Return the selected account type."""
        return self.account_type.currentText()

    def get_amount(self) -> str:
        """Return the amount input text."""
        return self.amount_input.text().strip()

    def update_balance(self, balance: float, account_str: str) -> None:
        """Update the balance display label."""
        self.balance_label.setText(f"Balance: ${balance:.2f}")

    def add_history_row(self, account: str, transaction: str, balance: float) -> None:
        """Add a row to the transaction history table."""
        row = self.history_table.rowCount()
        self.history_table.insertRow(row)
        self.history_table.setItem(row, 0, QTableWidgetItem(account))
        self.history_table.setItem(row, 1, QTableWidgetItem(transaction))
        self.history_table.setItem(row, 2, QTableWidgetItem(f"${balance:.2f}"))

    def show_status(self, message: str, color: str = "green") -> None:
        """Display a status message in the given color."""
        self.status_label.setText(message)
        self.status_label.setStyleSheet(f"color: {color};")

    def clear_amount(self) -> None:
        """Clear the amount input field."""
        self.amount_input.clear()

    def show_error(self, message: str) -> None:
        """Show an error dialog."""
        QMessageBox.critical(self, "Error", message)

    def show_info(self, message: str) -> None:
        """Show an info dialog."""
        QMessageBox.information(self, "Success", message)

    def connect_create(self, handler) -> None:
        """Connect the create button to a handler function."""
        self.create_button.clicked.connect(handler)

    def connect_deposit(self, handler) -> None:
        """Connect the deposit button to a handler function."""
        self.deposit_button.clicked.connect(handler)

    def connect_withdraw(self, handler) -> None:
        """Connect the withdraw button to a handler function."""
        self.withdraw_button.clicked.connect(handler)

    def connect_save(self, handler) -> None:
        """Connect the save button to a handler function."""
        self.save_button.clicked.connect(handler)