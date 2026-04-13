from django.db import models

# Create your models here.
class Students(models.Model) :  
    student_id = models.CharField(max_length=10) 
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=20) 

    def __str__(self):
        return self.name
        
class Employess(models.Model) : 
    emp_id = models.CharField(max_length=10) 
    name = models.CharField(max_length=100) 
    department = models.CharField(max_length=30) 
    designation = models.CharField(max_length=20) 

    def __str__(self) : 
        return self.name 
    
class Blog(models.Model) : 
    blog_title = models.CharField(max_length=100) 
    blog_body = models.TextField() 
    def __str__(self):
        return self.blog_title 
    

class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE , related_name='comments') 
    comment = models.TextField() 

    def __str__(self):
        return self.comment 
    
