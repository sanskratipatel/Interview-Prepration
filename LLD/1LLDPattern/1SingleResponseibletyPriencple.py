class User : 
    def __init__(self , name , age) : 
        self.__name = name 
        self.__age = age 
    
    def get_user_name(self) : 
        return f"User name is {self.__name}" 

    def is_user_allowed_to_vote(self) : 
        return self.__age > 18  
    
    def save_to_database(self) : 
        print(f"Connecting to DB") 
        print("Data is inserted") 

    def delete_to_database(self) : 
        return f"Delete from DB" 
u1 = User("BHI" , 43) 
print(u1.get_user_name()) 
print(u1.is_user_allowed_to_vote())   


class UserRepo : 
    def __init__(self , name , age) : 
        self.name = name 
        self.age = age 
    
    def get_user_name(self) : 
        return f"User name is {self.name}" 

    def is_user_allowed_to_vote(self) : 
        return self.age > 18  
    
     

class DBop : 
    def __init__(self , db , user , password) : 
        self.__db = db 
        self.__user = user 
        self.__password = password
    
    def save_to_database(self , user : UserRepo) : 
        print(f"User save in db {user.name}") 

    def delete_to_database ( self , user:UserRepo) :
        print(f"Delete from db {user.name}")
u1 = User("BHI" , 43) 
print(u1.get_user_name()) 
print(u1.is_user_allowed_to_vote())   

class UserRepo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_user_name(self):
        return f"User name is {self.name}"

    def is_user_allowed_to_vote(self):
        return self.age > 18


class DBop:
    def __init__(self, db, user, password):
        self.__db = db
        self.__user = user
        self.__password = password

    def save_to_database(self, user: UserRepo):
        print(f"Connecting to {self.__db}")
        print(f"User {user.name} saved in database")

    def delete_to_database(self, user: UserRepo):
        print(f"User {user.name} deleted from database")


u1 = UserRepo("BHI", 43)

print(u1.get_user_name())
print(u1.is_user_allowed_to_vote())

db = DBop("MySQL", "root", "1234")

db.save_to_database(u1)
db.delete_to_database(u1)