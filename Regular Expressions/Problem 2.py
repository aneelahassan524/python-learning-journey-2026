import re 

text = "Python is amazing"
text_1 = "I am learning Python"
result = re.match("Python",text)
result_1 = re.match("Python",text_1)

if result:
    print("Starts with Python")
else:
    print("Doesn't start with Python")

if result_1:
    print("Starts with Python")
else:
    print("Doesn't start with Python")    