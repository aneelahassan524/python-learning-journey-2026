import re

sentence = "Python is the best programming language."
result = re.search("programming",sentence)

if result:
    print("Word Found")
else:
    print("Word Not Found")
