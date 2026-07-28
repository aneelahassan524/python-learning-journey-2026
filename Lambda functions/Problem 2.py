#Add 15% GST:

new_list = []

prices = [100, 250, 500, 1000]
new_list = map(lambda price:price+(price*15/100),prices)

print(list(new_list))