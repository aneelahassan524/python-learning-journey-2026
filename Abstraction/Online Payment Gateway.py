from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self,amount):
        pass

class CreditCard(Payment):

    def pay(self,amount):
        self.amount = amount
        print(f"Amount Paid:{amount}")
        print("Processing Credit Card...")

class EasyPaisa(Payment):

    def pay(self,amount):
        self.amount = amount
        print(f"Amount Paid:{amount}")
        print("Processing EasyPaisa...")

class BankTransfer(Payment):

    def pay(self,amount):
        self.amount = amount
        print(f"Amount Paid:{amount}")
        print("Processing Bank Transfer...")

card = CreditCard()
paisa = EasyPaisa()
transfer = BankTransfer()
card.pay(5000)
paisa.pay(2500)
transfer.pay(10000)

