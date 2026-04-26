class User :
    def __init__(self , name ,age, email): 
        self.name = name 
        self.age = age 
        self.email = email 

    def get_user_info(self) : 
        print(f"This is {self.name} and my age is {self.age}") 

    def is_adult(self) ->bool:  
        return self.age>18 
    
    # This is Incorrect 
    # def save_to_database(self) : 
    #     print(f"Save to database {self.name}") 

    # def delete_to_database(self) :
    #     print("Delete from db " )



class UserCorrect :
    def __init__(self ,user , db , password): 
        self.db = db 
        self.user = user 
        self.password = password 
    
    def save_to_database(self , user : User) : 
        print(f"Save to database {user.name}") 

    def delete_to_database(self , user:User) :
        print("Delete from db " , user.name )


