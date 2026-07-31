#Convert this JSON into a Python dictionary.

import json
student = '{"name":"Sara","marks":95,"grade":"A"}'
result = json.loads(student)
print(result)
print(type(result))
