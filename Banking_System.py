#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Python code that simulates a basic banking system with multiple accounts, transactions, and a simple user interface.



class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds. Withdrawal canceled.")

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Added interest: ${interest}")


class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance=0, overdraft_limit=100):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds. Withdrawal canceled.")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_type, account_number):
        if account_type == "savings":
            account = SavingsAccount(account_number)
        elif account_type == "current":
            account = CurrentAccount(account_number)
        else:
            raise ValueError("Invalid account type. Choose 'savings' or 'current'.")
        
        self.accounts[account_number] = account
        print(f"Account created successfully. Account number: {account_number}")

    def get_account_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account.get_balance()
        else:
            print("Account not found.")













# Example usage:
bank = Bank()

bank.create_account("savings", "SA001")
bank.create_account("current", "CA001")

bank.accounts["SA001"].deposit(1000)
bank.accounts["CA001"].deposit(500)

bank.accounts["SA001"].add_interest()

bank.accounts["CA001"].withdraw(700)
print("Current Account Balance:", bank.get_account_balance("CA001"))


# In[ ]:




