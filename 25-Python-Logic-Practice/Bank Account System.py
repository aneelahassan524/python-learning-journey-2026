#Problem
#A bank wants to protect customers' account balances.

#Python Code:
class BankAccount:

    def __init__(self,account_holder,account_number):
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = 50000

    def deposit(self,amount):
        if(amount > 0):
            self.__balance = self.__balance+amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance =  self.__balance-amount

    def get_balance(self):
        return  self.__balance 
    
    def display_account(self):
        print("Bank Information:")
        print(f"Account Holder:{self.account_holder}")
        print(f"Account Number:{self.account_number}")
        print(f"Current Balance:{self.get_balance()}")

account1 = BankAccount("Aneela Hassan",1001)
account2 = BankAccount("Sara Ali",1002)
account1.deposit(6000)
account1.withdraw(2000)
account1.get_balance()
account1.display_account()
