def product_positive(list):
    if(list==[]):
        return 1
    if list[0] > 0:
        return list[0] * product_positive(list[1:])
    return product_positive(list[1:])
p = product_positive([20,-18,45,29,12,-79])
print(f"Product of Positive Numbers: {p}")
