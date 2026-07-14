customers = {
    "Ali": [2500, 1200, 800],
    "Sara": [5000, 1500],
    "Ahmed": [1000, 700, 900, 600],
    "Aneela": [4000, 2500],
    "Bilal": [1800]
}

highest_amount = 0
highest_customer = ""

for i in customers:
   total_amount = 0
   for j in customers[i]:
     total_amount = total_amount + j
     print(f"Total Amount of{i}:{total_amount}")

   if(total_amount>highest_amount):
        highest_amount = total_amount
        highest_customer = i

        print("\n===== Final Result =====")
        print(f"customer who spent the most money:{highest_customer}")
        print(f"Total Amount:{highest_amount}")
