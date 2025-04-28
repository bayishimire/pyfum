
class Customer:
    def __init__(self, name, bank_account, balance=0):
        self.name = name
        self.bank_account = bank_account
        self.balance = balance

    def show(self):
        return f"Bank account: {self.bank_account}, Name: {self.name}, Balance: {self.balance} thanks improve you saving "


class Bank(Customer):
    def __init__(self, name, bank_account, balance=0):
        super().__init__(name, bank_account, balance)

    def deposit(self, amount):
        if amount <= 0:
            print(f"{amount} is less than or equal to zero. Deposit failed.")
        else:
            self.balance += amount
            print(f"{amount} added. The new balance is {self.balance}")
class Withdraw(Customer):
    def getout (self, amount):
        if amount <= 0:
            print("Amount must be greater than zero. Withdrawal failed.")
        elif amount > self.balance:
            print("Insufficient funds. Withdrawal failed.")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. Remaining balance: {self.balance}")



# Main
name = input("Enter name: ")
bank_account = input("Enter bank account: ")
amount = int(input("Enter amount to deposit: "))
balance=0
# Create a Bank object
depositobject= Bank(name, bank_account,balance)

# Deposit the amount
depositobject.deposit(amount)

# Show account details
print(depositobject.show())
amount = int(input("Enter amount to withdraw: "))
withdraw_obj = Withdraw(name, bank_account, depositobject.balance)
withdraw_obj.getout(amount)
print(withdraw_obj.show())

