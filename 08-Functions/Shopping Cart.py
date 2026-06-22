def item(l1):
    i = 0
    max_item = l1[0]
    while (i < len(l1)):
        if l1[i] > max_item:
            max_item = l1[i]
        i += 1
    return f"The maximum item price is: {max_item}"

a = item([100, 250, 50, 200, 600, 90])
print(a)