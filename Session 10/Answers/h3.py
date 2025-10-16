class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner}'s account balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner}'s account balance: {self.balance}")
        else:
            print("Insufficient balance!")

# Test BankAccount
acc1 = BankAccount("Alice", 1000)
acc1.deposit(500)
acc1.withdraw(300)
acc1.withdraw(1500)
print()
