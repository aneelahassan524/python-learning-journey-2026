#Create a new dictionary where every student's marks increase by 10.

marks = {
    "Ali": 80,
    "Sara": 90,
    "Ahmed": 75
}
updated = {
    name : mark + 10
    for name,mark in marks.items()
}
print(updated)