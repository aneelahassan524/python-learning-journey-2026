def library (last_days):
    if(last_days<=0):
        return 0
    else:
        per_day = 20
        fine_amount = last_days*per_day
        return fine_amount
l = library(-5)    
print(f"The fine amount is:{l}")