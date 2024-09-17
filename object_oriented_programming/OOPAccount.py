
class Account:

    def __init__(self, owner, balance: float):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount
        print("Deposit accepted")

    def withdraw(self, amount: float):
        if amount > self.balance:
            print("Funds available")
        else:
            self.balance -= amount
            print("Withdraw accepted")
            print("Current balance: ${}".format(self.balance))

    def __str__(self):
        return "Account owner:  {}\nAccount balance: ${}".format(self.owner, self.balance)


acc1 = Account("Jose", 100)
print(acc1)
print(acc1.owner)
print(acc1.balance)
acc1.deposit(50)
acc1.withdraw(75)
acc1.withdraw(150)