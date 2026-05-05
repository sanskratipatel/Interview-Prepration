from abc import ABC ,abstractmethod 

class PayMethod(ABC) : 
    @abstractmethod
    def pay(self,amount :int) : 
        pass

class UPIPayment(PayMethod) :
    def pay(self,amount:int): 
        print(f"Paying threw UPI {amount}") 
    
class CreditCard(PayMethod):
    def pay(self ,amount : int):
        print(f"Paying threw CreditCard {amount}" ) 

class Paypal(PayMethod)  : 
    def pay(self, amount) :
         print(f"Paying threw Paypal {amount}" ) 
class NetBanking(PayMethod):
    def pay(self ,amount : int):
        print(f"Paying threw NetBanking {amount}" ) 

class PaymentProcess: 
    def process_payment(self,payment_method:PayMethod , amount): 
        payment_method.pay(amount)

upi = UPIPayment() 
credit = CreditCard() 
paypal = Paypal()
pay_method = PaymentProcess() 

pay_method.process_payment(paypal ,400)