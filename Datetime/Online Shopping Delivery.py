#A customer orders a product today.The company delivers it after 5 days.

from datetime import datetime,timedelta

print("=========== ORDER DETAILS ===========\n")

order_date = datetime.now()
print(f"Order Date   : {order_date.strftime('%d %B %Y')}")
delivery_date = order_date + timedelta(days=5)

print(f"Delivery Date: {delivery_date.strftime('%d %B %Y')}")
print("\nYour order will arrive in 5 days.")
