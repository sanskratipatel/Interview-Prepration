#  Interface Seggreration Principle 
#  Ensure That Classes are not Forced to implement 
# Methods that they dont need
from abc import ABC, abstractmethod  

class Employees(ABC) :  
    @abstractmethod 
    def eat (self) : 
        pass 
    @abstractmethod
    def work(self) :
        pass


class Worker(Employees) : 
    def eat(self) : 
        print("Worker is Eating") 
    
    def work(self):
        print("Employee is Working") 


class RobotWorker(Employees) :
    def work(self):
        print("Working") 
    
    def eat (self) :
        raise Exception("Error") 
