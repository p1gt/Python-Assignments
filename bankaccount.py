class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f'Balance: ${self.balance}')
        return self
    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self

oday = BankAccount(0.01)
awad = BankAccount(20, 100)

oday.deposit(1000).deposit(1000).deposit(200).withdraw(200).yield_interest().display_account_info()

awad.deposit(1000).deposit(1000).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()