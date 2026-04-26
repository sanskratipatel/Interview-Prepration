class Logger : 
    def __init__(self, file_name :str) : 
        self.file_name = file_name 
        self.log_count = 0 
    
    def log(self, text :str) : 
        print(f"Logger is Logging {text} in {self.file_name}")  
        self.log_count = self.log_count +1 

log1 = Logger("app.log")
log2 = Logger("app.log")
log3 = Logger("app.log") 

log1.log("First log") 
log2.log("Second log") 
log3.log("Third log")   
print(log1.log_count)
print(log2.log_count)
print(log3.log_count) 


class Logger: 
    __instance_variable = None 
    def __new__(cls , file_name):
        if cls.__instance_variable is None :
            cls.__instance_variable = super().__new__(cls)  
            cls.__instance_variable.file_name = file_name 
            cls.__instance_variable.log_count = 0 

            return cls.__instance_variable
        else : 
            return cls.__instance_variable
    def log(self,msg) : 
        print(f"Logging {msg} in {self.file_name} " ) 
        self.log_count +=1 
    def log_count1 (self) : 
        return self.log_count
log1 = Logger("app.log") 
print(log1.log_count1)     
log2 = Logger("app.log")
print(log2.log_count1)      
log3 = Logger("app.log") 
print(log3.log_count1) 
print() 
log1.log("First")
log2.log("Second")
log3.log("Third")

print(log1.log_count1())
print(log2.log_count1())
print(log3.log_count1())