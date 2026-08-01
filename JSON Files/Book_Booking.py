import json

book = {
    "title": "Python Mastery",
    "author": "Aneela",
    "price": 2500
}

with open ("book.json","w") as file:
    json.dump(book,file,indent=4)

with open("book.json", "r") as file:
    book = json.load(file)

print(book)
print(type(book))    