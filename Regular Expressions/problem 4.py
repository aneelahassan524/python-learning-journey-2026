#re.findall()
import re

data = """
employee: Ali
employee_id: EMP-1001
age: 24
salary: 85000
email: ali.khan@gmail.com
phone: 03001234567
username: ali_dev01

meeting_date: 25-06-2026
meeting_time: 10:30 AM

website:https://company.com

department:Software Development
"""
words = re.findall(r"\w+",data)
print(words)

space = re.findall(r"\s",data)
print(space)

find = re.findall(r".ing",data)
print(find)

start_match = re.findall(r"^employee",data)
print(start_match)


end_match = re.findall(r"Development$",data)
print(end_match)

more = re.findall(r"Dev*", data)
print(more)