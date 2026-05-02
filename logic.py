import csv
from PyQt6.QtWidgets import QFileDialog
from accounts import Account, SavingAccount
from gui import BankAppWindow


class BankController:
    """Connects the GUI to the Account logic. Controller in MVC pattern."""

    def __init__(self) -> None:
        """Initialize the controller with a window and no active account."""
        self.__window = BankAppWindow()
        self.__current_account = None
        self.__transactions: list = []

        self.__window.connect_create(self.__handle_create)
        self.__window.connect_deposit(self.__handle_deposit)
        self.__window.connect_withdraw(self.__handle_withdraw)
        self.__window.connect_save(self.__handle_save)

    def show(self) -> None:
        """Display the main application window."""
        self.__window.show()

    def __handle_create(self) -> None:
        """Validate input and create a new Account or SavingAccount."""
        name = self.__window.get_name()
        account_type = self.__window.get_account_type()

        if not name:
            self.__window.show_error("Account name cannot be empty.")
            return

        if account_type == "Savings Account":
            self.__current_account = SavingAccount(name)
        else:
            self.__current_account = Account(name)

        self.__transactions = []
        balance = self.__current_account.get_balance()
        self.__window.update_balance(balance, str(self.__current_account))
        self.__window.add_history_row(name, "Account Created", balance)
        self.__transactions.append([name, "Account Created", f"${balance:.2f}"])
        self.__window.show_status(f"{account_type} created for {name}!", "green")

    def __handle_deposit(self) -> None:
        """Validate input and deposit amount into the current account."""
        if not self.__check_account_exists():
            return

        amount_text = self.__window.get_amount()

        try:
            amount = float(amount_text)
        except ValueError:
            self.__window.show_error("Amount must be a number.")
            return

        if amount <= 0:
            self.__window.show_error("Deposit amount must be greater than 0.")
            return

        success = self.__current_account.deposit(amount)
        if success:
            balance = self.__current_account.get_balance()
            self.__window.update_balance(balance, str(self.__current_account))
            self.__window.add_history_row(
                self.__current_account.get_name(),
                f"Deposit: +${amount:.2f}",
                balance
            )
            self.__transactions.append([
                self.__current_account.get_name(),
                f"Deposit: +${amount:.2f}",
                f"${balance:.2f}"
            ])
            self.__window.show_status(f"Deposited ${amount:.2f} successfully.", "green")
        else:
            self.__window.show_error("Deposit failed.")

        self.__window.clear_amount()

    def __handle_withdraw(self) -> None:
        """Validate input and withdraw amount from the current account."""
        if not self.__check_account_exists():
            return

        amount_text = self.__window.get_amount()

        try:
            amount = float(amount_text)
        except ValueError:
            self.__window.show_error("Amount must be a number.")
            return

        if amount <= 0:
            self.__window.show_error("Withdrawal amount must be greater than 0.")
            return

        success = self.__current_account.withdraw(amount)
        if success:
            balance = self.__current_account.get_balance()
            self.__window.update_balance(balance, str(self.__current_account))
            self.__window.add_history_row(
                self.__current_account.get_name(),
                f"Withdrawal: -${amount:.2f}",
                balance
            )
            self.__transactions.append([
                self.__current_account.get_name(),
                f"Withdrawal: -${amount:.2f}",
                f"${balance:.2f}"
            ])
            self.__window.show_status(f"Withdrew ${amount:.2f} successfully.", "green")
        else:
            self.__window.show_error(
                "Withdrawal failed. Check amount or minimum balance rules."
            )

        self.__window.clear_amount()

    def __handle_save(self) -> None:
        """Open a file dialog and save transaction history to CSV."""
        if not self.__transactions:
            self.__window.show_error("No transactions to save.")
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self.__window, "Save Transactions", "", "CSV Files (*.csv)"
        )
        if not file_path:
            return

        try:
            with open(file_path, "w", newline="") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(["Account", "Transaction", "Balance After"])
                for row in self.__transactions:
                    writer.writerow(row)
            self.__window.show_info(f"Transactions saved to:\n{file_path}")
        except IOError as e:
            self.__window.show_error(f"Could not save file: {e}")

    def __check_account_exists(self) -> bool:
        """
        Check if an account has been created.

        Returns:
            bool: True if account exists, False otherwise.
        """
        if self.__current_account is None:
            self.__window.show_error("Please create an account first.")
            return False
        return True