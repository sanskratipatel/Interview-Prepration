class User : 
    name = "" 
    age = 0 
    gender = "" 
    def set_info(self) : 
        self.name = input("Enter your name ") 
        self.age = (input("Enter age ")) 
        self.gender(input("Enter gender ")) 

    def display(self)  : 
        print(f"my NAME IS {self.name} {self.age} {self.gender}")
u1 = User() 

print(u1.name) 
u1.display()  
u1.set_info()