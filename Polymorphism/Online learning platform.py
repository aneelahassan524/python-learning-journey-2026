class Registration:

    def  register(self,name,email=None,phone_number=None):
        
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def display(self):
       
        print("Student Registration Details:")
        if(self.name ):
          print(f"Name:{self.name}")
        if(self.email):
            print(f"Email:{self.email}")
        if(self.phone_number):
            print(f"Phone Number:{self.phone_number}\n")

reg = Registration()
reg.register("Saba")
reg.display()
reg.register("Aneela","Aneela456@gmail.com")
reg.display()
reg.register("Anum","Anum789@gmail.com","03005151511")
reg.display()