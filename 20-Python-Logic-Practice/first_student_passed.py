students = {
    "Raza": 25,
    "Sara": 35,
    "Ahmed": 80,
    "Aneela": 90
}
for name in students:
    marks = students[name]
    if(marks>=40):
      print(f"First student passed:{name}")
      break      