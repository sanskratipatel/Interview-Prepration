# # Child class Should not break parent class behaviour 
from abc import ABC ,abstractmethod
# class BankAccount(ABC) :
#     def __init__(self,balance :int): 
#         self.balance = balance 
#     @abstractmethod
#     def withdraw(self): 
#         pass 
#     @abstractmethod
#     def deposit(self) :  
#         pass


# class SavingAccount(BankAccount) : 
#     def __init__(self, balance): 
#         super().__init__(balance)
    
#     def withdraw(self , amount):
#         if self.balance < amount : 
#            print("Insufficient Balance")  
#         else: 
#             self.balance = self.balance-amount 
#             print("Amount Withdrwa Remaining Amount ",self.balance) 

    
#     def deposit(self ,amount) : 
#        self.balance = self.balance+ amount 
#        print("Amount Deposit")


# class FD(BankAccount) : 
#     def __init__(self,balance): 
#         super().__init__(balance) 
    
#     def deposit(self,amount): 
#         self.balance = self.balance -amount  
#         print("Your Balance is ", self.balance)

#     def withdraw(self,amount):
#         raise Exception ("Cannot Withdraw !!!!!!!!! ") 


        
# s= SavingAccount(1000) 

# s.deposit(500)
# s.withdraw(400) 
# e1 =FD(1000) 
# e1.withdraw(500)
        
class Account(ABC) : 
    def __init__(self,balance):  
        self.balance = balance 
    @abstractmethod
    def deposit(self): 
        pass


class Withdraw_Accounts(Account):
    def __init__(self,balance) :  
        super().__init__(balance) 
    @abstractmethod
    def withdraw(self ,amount) : 
         pass

class SavingAmount(Withdraw_Accounts) : 
    def __init__(self,balance) : 
        super().__init__(self,balance) 
    
    def deposit(self ,amount): 
       self.balance = self.balance - amount 
       print(f"Amount Deposit ,current Balance = ",self.balance) 

    def withdraw(self, amount):
        if self.balance <amount: 
            print("Noooooo")
        else : 
            self.balance =self.balance-amount
            print("Yayyyyyyy") 

        
class FixedAccount(Account) : 
    def __init__(self, balance):
        super().__init__(balance) 
    
    def deposit(self ,amount):
        self.balance = self.balance - amount 
        print(f"Amount Deposit ,current Balance = ",self.balance) 

        
       


        