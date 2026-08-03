#re.findall()
import re

text = "Math: 78 English: 91 Science: 84 Computer: 99"
result = re.findall(r"\d+",text)

print(result)