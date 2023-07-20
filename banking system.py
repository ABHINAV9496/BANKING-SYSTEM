#Write a python program to replicate a Banking system.The following features are mandatory:
#1.Account Login
#2.Account Depositing
#3.withdrawl

class BankAccount:
    def __init__(self, account_number, pin):
        self.account_number = account_number
        self.pin = pin
        self.balance = 0.0

    def login(self, account_number, pin):
        if self.account_number == account_number and self.pin == pin:
            return True
        else:
            return False

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} successfully. Current balance: {self.balance:}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount} successfully. Current balance: {self.balance:}")
        else:
            print("Insufficient balance.")


account = BankAccount("123456789", "1234")


# Login
account_number = input("Enter your account number: ")
pin = input("Enter your PIN: ")
if account.login(account_number, pin):
    print("Login successful.")
else:
    print("Invalid account number or PIN.")

# Deposit
amount = float(input("Enter the amount to deposit: "))
account.deposit(amount)

# Withdrawal
amount = float(input("Enter the amount to withdraw: "))
account.withdraw(amount)
