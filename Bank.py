class Account:
    def __init__(self, account_number, pin, balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def withdraw_cash(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal successful. Remaining balance: ${self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

    def check_balance(self):
        return f"Current balance: ${self.balance}"

class Transaction:
    def __init__(self, user, account, transaction_type, amount):
        self.user = user
        self.account = account
        self.transaction_type = transaction_type
        self.amount = amount

    def execute_transaction(self):
        if self.transaction_type == "withdraw":
            return self.account.withdraw_cash(self.amount)
        elif self.transaction_type == "check_balance":
            return self.account.check_balance()
        else:
            return "Invalid transaction type."

class User:
    def __init__(self, username, pin):
        self.username = username
        self.pin = pin
        self.account = None

    def set_account(self, account):
        self.account = account

# ATM class to simulate the ATM system
class ATM:
    def __init__(self):
        self.users = []

    def create_user(self, username, pin, account_number, initial_balance):
        user = User(username=username, pin=pin)
        account = Account(account_number=account_number, pin=pin, balance=initial_balance)
        user.set_account(account)
        self.users.append(user)
        return user

    def verify_pin(self, user, entered_pin):
        return user.pin == entered_pin

    def perform_transaction(self, user, transaction_type, amount=None):
        if user.account:
            if self.verify_pin(user, int(input("Enter your PIN: "))):
                transaction = Transaction(user, user.account, transaction_type, amount)
                return transaction.execute_transaction()
            else:
                return "Incorrect PIN. Transaction failed."
        else:
            return "User does not have an account."

# Example usage:
atm = ATM()

# Create a user with an account
user1 = atm.create_user(username="JohnDoe", pin=1234, account_number="123456789", initial_balance=1000)

# Perform transactions
result1 = atm.perform_transaction(user1, transaction_type="withdraw", amount=200)
print(result1)

result2 = atm.perform_transaction(user1, transaction_type="check_balance")
print(result2)
