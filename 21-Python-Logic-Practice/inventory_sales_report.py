inventory = {
    "Rice": [50, 15],
    "Sugar": [20, 25],
    "Oil": [35, 10],
    "Tea": [10, 40],
    "Soap": [60, 8]
}

highest_revenue = 0
highest_product = ""
for product in inventory:
    
     quantity = inventory[product][0]
     price = inventory[product][1]
     total_revenue = quantity*price
     
     if(total_revenue>highest_revenue):
          highest_revenue = total_revenue
          highest_product = inventory[product]
          
          print(f"Highest Revenue:{highest_revenue}")
          print(f"Highest Product:{[product]}")
          