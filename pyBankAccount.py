class BankAccount:
    """Represents a bank account with basic deposit, withdrawal, and balance viewing features."""

    def __init__(self, account_number, account_holder_name, initial_balance = 0.0):
        """
        Initializes a new BankAccount.

        Args:
            account_number (int): The account id number.
            account_holder_name (str): The name of the account holder.
            initial_balance (float): The starting balance. Defaults to 0.0.
        """
        # Public attributes
        self.account_number = account_number
        self.account_holder_name = account_holder_name

        # Internal attributes
        # _balance
        if initial_balance < 0:
            print("Error: Initial balance cannot be a negative number.")
            print("Setting initial balance to 0.0")
            self._balance = 0.0 
        else:
            self._balance = initial_balance

    def deposit(self, amount):
        """
        Deposits money into the bank account.

        Args:
            amount (float): The amount of money to be deposited into the account.
        """
        while True:
            try:
                amount = float(amount)
                if amount < 0:
                    print("Error: deposit amount must be greater than 0.")
                    amount = input("Enter the amount you would like to deposit: $")
                else:
                    self._balance += amount
                    print(f"Successfully deposited ${amount:.2f}. Your new account balance is ${self._balance:.2f}.")
                    break
            except ValueError:
                print("Error: Enter a valid number.")
                amount = input("Enter the amount you would like to deposit: $")

    def withdraw(self, amount):
        """
        Withdraws money from the bank account.

        Args:
            amount (float): The amount of money to be withdrawn from the bank account.
        """
        while True:
            try:
                amount = float(amount)
                if amount > 0:
                    if amount <= self._balance:
                        self._balance -= amount
                        print(f"Successfully withdrew ${amount:.2f}. Remaining balance is ${self._balance:.2f}.")
                        break
                    else:
                        print(f"Error: Unable to withdraw more than your current balance of ${self._balance:.2f}.")
                        amount = input("Enter the amount you would like to withdraw: $")
                else:
                    print("Error: Withdraw amount must be greater than 0.")
                    amount = input("Enter the amount you would like to withdraw: $")
            except ValueError:
                print("Error: Enter a valid number.")
                amount = input("Enter the amount you would like to withdraw: $")

    @property
    def balance(self):
        """
        Returns the current balance of the bank account.
        """
        return self._balance
    
    # Display account information
    def display_account_details(self):
        """
        Displays the bank account details in an easy to read format.
        """
        print(f"   Account Holder's Name: {self.account_holder_name}")
        print(f"   Account Number: {self.account_number}")
        print(f"   Current Balance: ${self.balance}")

    def __str__(self):
        """
        Returns the bank acount details in an easy to read format.
        """
        return f"   Account Holder's Name: {self.account_holder_name}\n   Account Number: {self.account_number}\n   Current Balance: ${self.balance}"
    
# Implementation

# Initialize new object of BankAccount
bank_account = BankAccount(1234, "Tony Bologna")
print("Bank account initialized.\n")

# Deposit Money
bank_account.deposit(input("Enter the amount you would like to deposit: $"))

# Withdraw Money
bank_account.withdraw(input("Enter the amount you would like to withdraw: $"))

# Testing Encapsulation
bank_account._balance = 1000

# Display account details
print(bank_account)
print("\n")
bank_account.display_account_details()