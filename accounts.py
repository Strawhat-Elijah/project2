class Account:
    """Represents a basic bank account with deposit and withdraw functionality."""

    def __init__(self, name: str, balance: float = 0) -> None:
        """
        Initialize an Account object.

        Args:
            name (str): The account holder's name.
            balance (float): The starting balance (default 0).
        """
        self.__account_name: str = name
        self.__account_balance: float = 0
        self.set_balance(balance)

    def deposit(self, amount: float) -> bool:
        """
        Deposit an amount into the account.

        Args:
            amount (float): The amount to deposit.

        Returns:
            bool: True if successful, False otherwise.
        """
        if amount <= 0:
            return False
        self.__account_balance += amount
        return True

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw an amount from the account.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if successful, False otherwise.
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        self.__account_balance -= amount
        return True

    def get_balance(self) -> float:
        """Return the current account balance."""
        return self.__account_balance

    def get_name(self) -> str:
        """Return the account holder's name."""
        return self.__account_name

    def set_balance(self, value: float) -> None:
        """
        Set the account balance.

        Args:
            value (float): The new balance. Set to 0 if negative.
        """
        if value < 0:
            self.__account_balance = 0
        else:
            self.__account_balance = value

    def set_name(self, value: str) -> None:
        """
        Set the account holder's name.

        Args:
            value (str): The new name.
        """
        self.__account_name = value

    def __str__(self) -> str:
        """Return a string representation of the account."""
        return f"Account Name: {self.get_name()}, Balance: ${self.get_balance():.2f}"


class SavingAccount(Account):
    """
    Represents a savings account with a minimum balance and interest rate.
    Inherits from Account.
    """

    MINIMUM: float = 100
    RATE: float = 0.02

    def __init__(self, name: str) -> None:
        """
        Initialize a SavingAccount object.

        Args:
            name (str): The account holder's name.
        """
        super().__init__(name, SavingAccount.MINIMUM)
        self.__deposit_count: int = 0

    def apply_interest(self) -> None:
        """Apply 2% interest to the current balance."""
        interest = self.get_balance() * SavingAccount.RATE
        self.set_balance(self.get_balance() + interest)

    def deposit(self, amount: float) -> bool:
        """
        Deposit an amount and apply interest every 5 deposits.

        Args:
            amount (float): The amount to deposit.

        Returns:
            bool: True if successful, False otherwise.
        """
        if amount <= 0:
            return False
        super().deposit(amount)
        self.__deposit_count += 1
        if self.__deposit_count % 5 == 0:
            self.apply_interest()
        return True

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw an amount, ensuring balance stays above minimum.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if successful, False otherwise.
        """
        if amount <= 0:
            return False
        if self.get_balance() - amount < SavingAccount.MINIMUM:
            return False
        super().withdraw(amount)
        return True

    def set_balance(self, value: float) -> None:
        """
        Set the balance, enforcing the minimum balance rule.

        Args:
            value (float): The new balance.
        """
        if value < SavingAccount.MINIMUM:
            super().set_balance(SavingAccount.MINIMUM)
        else:
            super().set_balance(value)

    def __str__(self) -> str:
        """Return a string representation of the savings account."""
        return f"Saving Account Name: {self.get_name()}, Balance: ${self.get_balance():.2f}"