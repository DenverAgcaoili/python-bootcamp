class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self,amount):
        self.balance = self.balance + amount

    def withdraw(self,amount):
        self.balance = self.balance - amount

    def print_balance(self):
        print(self.balance)

account_1 = BankAccount()
print(account_1.balance)

account_1.deposit(1_000)
print(account_1.balance)

account_1.withdraw(500)
print(account_1.balance)