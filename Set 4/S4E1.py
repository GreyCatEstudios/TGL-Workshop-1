class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
            return
        self.balance -= amount
        return self.balance

    def check_balance(self):
        return self.balance


# Testing the class
account = BankAccount()
print("Deposit 100:", account.deposit(100))    # prints: Deposit 100: 100
print("Withdraw 50:", account.withdraw(50))   # prints: Withdraw 50: 50
print("Withdraw 60:", account.withdraw(60))   # prints: Insufficient balance!
print("Check Balance:", account.check_balance())  # prints: Check Balance: 50
