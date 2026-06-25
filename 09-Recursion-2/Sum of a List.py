def sum_list(list):
    if(list==[]):
        return 0
    return list[0] + sum_list(list[1:])
s = sum_list([10,29,31,12,6])
print(f"Sum of a List:{s}")