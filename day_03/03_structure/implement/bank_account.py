class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")

        self.__balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError()

        self.__balance -= amount

    def print_balance(self):
        print(self.__balance)


account_1 = BankAccount()
account_1.print_balance()

account_1.deposit(100)
account_1.__balance = 200
account_1.print_balance()
