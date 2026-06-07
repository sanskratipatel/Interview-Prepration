from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager
# Create your models here.
class MyUserManager(BaseUserManager) : 
    def create_user(self,email,name, tc, password=None , password2=None) : 
        if not email : 
            raise ValueError('User must have an email address')  
        user = self.model( 
            email = self.normalize_email(email) , 
            name = name ,
            tc = tc 
        )  
        user.set_password(password) 
        user.save(using = self.db)  
        return user


    def create_superuser(self, email,name, tc ,password = None) :  
        user = self.create_user( 
            email, 
            password = password ,  
            tc =tc ,
            name = name

        ) 
        user.is_admin = True 
        user.is_superuser = True
        user.save(using =self.db) 
        return user


       
class User(AbstractUser) : 
    username = None
    email = models.EmailField(verbose_name='email address' , max_length=255,unique=True) 
    date_of_birth = models.DateField(null=True, blank=True) 
    name = models.CharField(max_length=255)
    tc = models.BooleanField()
    is_active = models.BooleanField(default=True) 
    is_admin = models.BooleanField(default=False) 
    created_At = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
      
    objects = MyUserManager()
    USERNAME_FIELD ='email' 
    REQUIRED_FIELDS=['name','tc'] 
    def __str__(self):
        return self.email  
    
    def has_perm(self, perm, obj=None):
      return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self) : 
        return self.is_admin
         
