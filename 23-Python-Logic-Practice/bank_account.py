#Problem : A bank wants to manage customer accounts.
class BankAccount:

    bank_name = "Meezan Bank"

    def __init__(self,account_holder,account_number,balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def display_account(self):
        print(f"Account Holder:{self.account_holder}\nAccount Number:{self.account_number}\nBalance:{self.balance}")

    def deposit(self,amount):
        self.balance  = self.balance+amount
        print("Deposit Successful")

    def withdraw(self,amount):
        if(self.balance>amount):  
            self.balance  = self.balance-amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    @ classmethod
    def show_bank(cls):
        print(f"Bank Name:{cls.bank_name}")  

    @ staticmethod
    def minimum_balance():
        print("Minimum Balance Required = 500")

account1 = BankAccount("Ahmed Khan", 1001001, 25000)
account2 = BankAccount("Sara Ali", 1001002, 42000)
account3 = BankAccount("Aneela Hassan", 1001004, 65000)

account1.display_account()
account2.deposit(5000) 
account3.withdraw(6000) 
account2.show_bank()
account3.minimum_balance()