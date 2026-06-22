def withdrawal (balance,withdraw_amount):
    if(balance < withdraw_amount):
        print("Transaction Failed: Insufficient funds in your account")
    else:
        new_balance = balance-withdraw_amount
        return new_balance
w = withdrawal(10000,4000)
print(f"The New Balance is:{w}")
    