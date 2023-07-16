# Write a python program to replicate a Banking system. The following features are mandatory:
# 1.Account login
# 2. Amount Depositing
# 3. Amount Withdrawal


import re


class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into account {self.account_number}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}.")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.balance


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_number, account_holder):
        account = BankAccount(account_number, account_holder)
        self.accounts.append(account)
        print(f"Account {account_number} created for {account_holder}.")

    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None


def is_valid_account_number(account_number):
    # Simple validation: 8 digits
    pattern = r"^\d{8}$"
    return re.match(pattern, account_number) is not None


def main():
    bank = Bank()

    while True:
        print("\n=== Banking System ===")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number (8 digits): ")
            if not is_valid_account_number(account_number):
                print("Invalid account number format. Account number should be 8 digits.")
                continue

            account_holder = input("Enter account holder name: ")
            bank.create_account(account_number, account_holder)

        elif choice == "2":
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account is None:
                print("Invalid account number.")
                continue

            print(f"Welcome, {account.account_holder}!")
            while True:
                print("\n1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Logout")

                option = input("Enter your option: ")

                if option == "1":
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)

                elif option == "2":
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)

                elif option == "3":
                    balance = account.get_balance()
                    print(f"Account Balance: {balance}")

                elif option == "4":
                    print("Logged out.")
                    break

                else:
                    print("Invalid option.")

        elif choice == "3":
            print("Thank you for using the banking system.")
            break

        else:
            print("Invalid choice. Please try again.")


main()
