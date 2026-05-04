from django.db import models
import uuid
# Create your models here.
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser) : 
    pass 

class Product(models.Model) : 
    name = models.CharField(max_length=200) 
    description = models.TextField() 
    price = models.DecimalField(max_length=10,decimal_places=2) 
    stock = models.PositiveIntegerField()
    # image = models.ImageField(upload_to='products/' , blank=True , null = True)   
    price = models.PositiveBigIntegerField()

    @property 
    def in_stock(self) : 
        return self.stock > 0  
    
    def __str__(self):
        return self.name 
    

class Order(models.Model) : 
    class Statues(models.TextChoices): 
        PENDING = 'Pending' 
        CONFIRMED = 'Confirmed' 
        CANCELLED ='Cancelled'  
    
    order_id = models.UUIDField(primary_key=True , default=uuid.uuid4) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    created_at = models.DateTimeField(auto_now_add=True) 
    status = models.CharField(max_length=10 ,choices =Statues,default=Statues.PENDING ) 
    products =models.ManyToManyField(Product , through='OrderItem',related_name='orders') 

     
    def __str__(self) : 
        return f"Order {self.order_id} and user_name is f{self.user.username}"

class OrderItem(models.Model) : 
    order = models.ForeignKey(Order , on_delete=models.CASCADE) 
    product = models.ForeignKey(Product,on_delete=models.CASCADE) 
    quantity = models.PositiveBigIntegerField() 

    @property 
    def item_subtotal(self) : 
        return self.product.price * self.quantity  
    
    def __str__(self):
        return f"{self.quantity} X {self.product.name} in order {self.order.order_id}"
    

    
