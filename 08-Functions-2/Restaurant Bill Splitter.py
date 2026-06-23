def split_bill (total_bill,total_friends):
    if(total_friends==0):
        return "Invalid Input"
    calculate_share = total_bill/total_friends
    return calculate_share
b = split_bill(7000,0)
print(f"Share of each friend:{b}")
