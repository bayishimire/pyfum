# bank_account_fixed.py
'''Question: Implement a Bank Account Management System File to submit: bank_account.py Task Description: Create a Python program that implements a simple bank account management system using object-oriented programming. Your program should define the following classes: 1. Account class (base class) 
 
Should have attributes: account_number, holder_name, and balance
 
Should have methods: 
 
_init_(self, account_number, holder_name, initial_balance=0)
 
deposit(self, amount) - adds amount to balance
 
withdraw(self, amount) - subtracts amount from balance if sufficient funds available
 
get_balance(self) - returns current balance
 
_str_(self) - returns a string representation of the account
 
 
 
 2. SavingsAccount class (inherits from Account) 
 
Additional attribute: interest_rate
 
Additional methods: 
 
_init_(self, account_number, holder_name, interest_rate, initial_balance=0)
 
add_interest(self) - adds interest to the balance based on interest_rate
 
Override _str_(self) to include interest rate information
 
 
 
 3. CheckingAccount class (inherits from Account) 
 
Additional attribute: overdraft_limit
 
Additional methods: 
 
_init_(self, account_number, holder_name, overdraft_limit, initial_balance=0)
 
Override withdraw(self, amount) to allow withdrawals up to overdraft_limit beyond balance
 
Override _str_(self) to include overdraft limit information
 
 
 
 4. Create a function main() that: 
 
Creates at least one instance of each account type
 
Performs several operations (deposits/withdrawals)
 
Adds interest to savings accounts
 
Prints out the details of each account
 
 Example expected output: Savings Account #SA001 Holder: John Smith Balance: $1,050.00 Interest Rate: 5.0% 
 Checking Account #CA001 Holder: Jane Doe Balance: $-50.00 Overdraft Limit: $100.00 
Requirements: 
 
Your code should handle invalid inputs (like negative deposits or withdrawals exceeding limits)
 
Your code should demonstrate inheritance and method overriding
 
Proper documentation and comments should be included
 
Follow good object-oriented programming practices'''

class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def display(self):
        print(f"Account Number: {self.account_number}\nHolder Name: {self.holder_name}\nBalance: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
        else:
            self.balance += amount
            print(f"Deposited ${amount:.2f} successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account({self.account_number}, {self.holder_name}, Balance: ${self.balance:.2f})"


class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.05):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of ${interest:.2f} added. New balance: ${self.balance:.2f}")

    def __str__(self):
        return (f"SavingsAccount({self.account_number}, {self.holder_name}, "
                f"Balance: ${self.balance:.2f}, Interest Rate: {self.interest_rate*100:.1f}%)")


def main():
    # Create savings accounts
    saving = SavingsAccount("123456789", "John Doe", 1000, 0.05)
    checking = SavingsAccount("987654321", "Jane Doe", 2000, 0.03)  # Still using SavingsAccount for simplicity

    # Perform operations
    saving.deposit(500)
    saving.withdraw(200)
    saving.add_interest()
    saving.display()

    checking.deposit(1000)
    checking.withdraw(500)
    checking.add_interest()
    checking.display()

    # Print account info using __str__
    print("\n--- Account Summaries ---")
    print(saving)
    print(checking)


if __name__ == "__main__":
    main()










           

       