with open ("student.txt","r") as file:
    data = file.read()
    if("Aneela Hassan" in data):
        print("Student Found")
    else:
        print("Student Not Found")    
