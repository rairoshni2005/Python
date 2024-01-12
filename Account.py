class Bank:
    def __init__(self):
        # Initialize an empty dictionary to represent customer accounts
        self.accounts = {}

    def create_account(self, account_number, customer_name, initial_balance=0):
        # Create a new customer account
        if account_number not in self.accounts:
            self.accounts[account_number] = {'customer_name': customer_name, 'balance': initial_balance}
            print(f"Account created for {customer_name} with account number {account_number}.")
        else:
            print("Account number already exists. Please choose a different account number.")

    def deposit(self, account_number, amount):
        # Deposit money into a customer account
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            print(f"Deposited ${amount} into account {account_number}.")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        # Withdraw money from a customer account
        if account_number in self.accounts:
            if self.accounts[account_number]['balance'] >= amount:
                self.accounts[account_number]['balance'] -= amount
                print(f"Withdrew ${amount} from account {account_number}.")
            else:
                print("Insufficient funds.")
        else:
            print("Account not found.")

    def check_balance(self, account_number):
        # Check the balance of a customer account
        if account_number in self.accounts:
            balance = self.accounts[account_number]['balance']
            print(f"Balance in account {account_number}: ${balance}.")
        else:
            print("Account not found.")

    def transfer_money(self, sender_account, receiver_account, amount):
        # Transfer money between customer accounts
        if sender_account in self.accounts and receiver_account in self.accounts:
            if self.accounts[sender_account]['balance'] >= amount:
                self.accounts[sender_account]['balance'] -= amount
                self.accounts[receiver_account]['balance'] += amount
                print(f"Transferred ${amount} from account {sender_account} to account {receiver_account}.")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("One or both accounts not found.")

# Example usage:
bank = Bank()

bank.create_account(account_number="1001", customer_name="John Doe", initial_balance=1000)
bank.create_account(account_number="1002", customer_name="Jane Smith", initial_balance=1500)

bank.deposit(account_number="1001", amount=500)
bank.withdraw(account_number="1002", amount=200)
bank.check_balance(account_number="1001")
bank.check_balance(account_number="1002")

bank.transfer_money(sender_account="1001", receiver_account="1002", amount=300)

bank.check_balance(account_number="1001")
bank.check_balance(account_number="1002")
