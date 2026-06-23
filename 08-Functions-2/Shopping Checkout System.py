def subtotal(item_1, item_2, item_3, item_4):
    return item_1 + item_2 + item_3 + item_4

def discount(total):
    return total * 20 / 100

def after_discount(total):
    return total - discount(total)

def tax(amount):
    return amount * 5 / 100

def final_amount(item_1, item_2, item_3, item_4):
    total = subtotal(item_1, item_2, item_3, item_4)
    after_disc = after_discount(total)
    tax_amount = tax(after_disc)
    return after_disc + tax_amount

a = final_amount(100, 200, 150, 60)
print(f"Final Payable Amount: {a}")