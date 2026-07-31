#Convert it into JSON using json.dumps().
import json

book = {
    "title": "Python Basics",
    "author": "Harry",
    "price": 1500
}
result = json.dumps(book)
print(result)
print(type(result))

