def count_positive(list):
    if(list==[]):
        return 0
    if list[0] > 0:
     return 1 + count_positive(list[1:])
    else:
     return count_positive(list[1:])
c = count_positive([12,41,-20,35,-15])
print(f"Count Positive Numbers in a List:{c}")
    