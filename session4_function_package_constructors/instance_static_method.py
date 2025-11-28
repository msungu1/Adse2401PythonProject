# python script to demonstrate the use of instances, static and class methods in a real-world scenario

import re

class BankAccount:
    # a class attribute (shared across all instances)
    interest_rate = 0.05   # 5% annual interest rate

    # constructor
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    # ------------------------------------------------------------------------
    # instance methods
    # ------------------------------------------------------------------------
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            # display the new balance
            print(f"[{self.account_holder}] deposited Kes. {amount:.2f}"
                  f"\nNew balance is: Kes. {self.balance:.2f}")
        else:
            print("Kindly note that the deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:  # shortened condition
            self.balance -= amount
            # display the amount withdrawn and new balance
            print(f"[{self.account_holder}] withdrew Kes. {amount:.2f}"
                  f"\nNew balance is: Kes. {self.balance:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient balance!")

    # ------------------------------------------------------------------------
    # class methods
    # ------------------------------------------------------------------------
    @classmethod
    def set_interest_rate(cls, new_rate):
        if 0 < new_rate <= 0.2:
            cls.interest_rate = new_rate
            # notify about the change in annual interest rate
            print(f"The annual interest rate has been set to {new_rate * 100:.0f}% for all accounts!")
        else:
            print("The annual interest rate must be between 0% and 20%!")

    # ------------------------------------------------------------------------
    # static methods
    # ------------------------------------------------------------------------
    @staticmethod
    def validate_account_number(account_number):
        # regex pattern to ensure the account starts with 'ACC' followed by 6 digits
        pattern = r"^ACC\d{6}$"
        return bool(re.match(pattern, account_number))


# ------------------------------------------------------------------------------------------
# Demonstrate the BankAccount class and its instance, class, and static methods
# ------------------------------------------------------------------------------------------

# create 2 bank account objects
abigail_acc = BankAccount("ABIGAIL", 55000.00)
brian_acc = BankAccount("BRIAN", 15000.00)

# deposit and withdraw money into and from Abigail's and Brian's accounts
abigail_acc.deposit(5000)
abigail_acc.withdraw(12000)

brian_acc.deposit(3000)
brian_acc.withdraw(20000)  # should fail due to insufficient balance

# change interest rate using class method
BankAccount.set_interest_rate(0.1)

# validate account numbers using static method
print("Account number validation:")
print("ACC123456 is valid?", BankAccount.validate_account_number("ACC123456"))
print("XYZ987654 is valid?", BankAccount.validate_account_number("XYZ987654"))
