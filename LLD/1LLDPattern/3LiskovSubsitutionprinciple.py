from abc import ABC ,abstractmethod 
 

class Amount(ABC) : 
    def __init__(self,balance) : 
        self.balance = balance  
    @abstractmethod
    def deposit(self , amount) : 
        pass 

class WithdrawableAccount(Amount): 
    def __init__(self , balance) : 
        super().__init__(balance)  
    @abstractmethod
    def withdrwa(self,amount):
        pass

class Saving(WithdrawableAccount):
    def __init__(self,balance) : 
        super().__init__(balance) 
    
    def deposit(self, amount) : 
        self.balance = self.balance + amount 
        print(f"{amount} deposit sunccessfully now balance is {self.balance}" ) 
    
    def  withdrwa(self,amount):
        if self.balance >= amount : 
            self.balance = self.balance - amount  
            print(f"{amount} wothdrw sunccessfully now balance is {self.balance}" )  
        else : 
            print(f"You dont have this much balance to withdrwa")
    
s = Saving(1000)

s.deposit(500)
s.withdrwa(700)
s.withdrwa(1000)