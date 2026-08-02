class PaymentProcessor: 
    def pay(self , payment_method , amount) : 
        if payment_method == "UPI" : 
            print(f"Payment threw upi"  , amount) 
            print(f"Transction Done" ) 
        elif payment_method == "credit_card" : 
            print(f"Payment threw credit card"  , amount) 
            print(f"Transction Done" )  
        elif payment_method == "net_banking" : 
            print(f"Payment threw net_banking"  , amount) 
            print(f"Transction Done" )  
            
pay_p = PaymentProcessor() 
print("credit" , pay_p.pay("UPI" ,500)) 

from abc import ABC , abstractmethod 

class  PaymentMethod(ABC): 
    @abstractmethod
    def pay_money(self , amount)  : 
        pass
    
class UPIPayment(PaymentMethod) : 
    def pay_money(self , amount) : 
        print(f"Paying through UPI of amount") 

    
class CreditCardPayment(PaymentMethod) : 
    def pay_money(self , amount) : 
        print(f"Paying through CreditCardPayment  of amount") 

    
class PaypalPayment(PaymentMethod) : 
    def pay_money(self , amount) : 
        print(f"Paying through PaypalPayment  of amount")  

class PaymentProcessing:
    def process_payment(self, payment_method : PaymentMethod , amount) : 
        payment_method.pay_money(amount)