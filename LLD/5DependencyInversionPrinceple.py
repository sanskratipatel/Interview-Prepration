class EmailService: 
    def send_email (self , message) : 
        print("Sending Mail") 
    
class SMSService: 
    def send_sms(self, message) : 
        print("Sending Sms") 
from abc import ABC, abstractmethod

class NotificationService(EmailService , SMSService) : 
    def __init__(self ): 
        self.email_serive = EmailService()  
        self.sms_service = SMSService() 

    def notify_email(self,message):
        self.email_serive.send_email(message) 
    
    def notify_msm(self,message) :
         self.sms_service.send_sms(message)


d1 = NotificationService() 
d1.notify_email("Hello") 
d1.notify_msm("Ji") 

class NotificationChannel(ABC) : 
    @abstractmethod
    def send(self , message): 
        pass

class EmailServiceC(NotificationChannel): 
    def send(self , message) : 
        print("Sending Mail yaha se ", message) 
    
class SMSServiceC(NotificationChannel): 
    def send(self, message) : 
        print("Sending Sms") 

class NotificationNew:
    def __init__(self, channel:NotificationChannel): 
        self.channel = channel 

    def notify(self,message) : 
        self.channel.send(message)
e1 = EmailServiceC() 
s1 = SMSServiceC()
w1 = NotificationNew(e1) 
w1.notify("Hello")