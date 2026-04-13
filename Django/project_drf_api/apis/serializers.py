from rest_framework import serializers 
from apis.models import Students ,Employess,Blog,Comments


class StudentSerializers(serializers.ModelSerializer): 
    class Meta:
        model = Students 
        fields = "__all__" 

    
class EmployeesSerializers(serializers.ModelSerializer) :
    class Meta:
        model = Employess 
        fields = "__all__" 

class CommentSerializers(serializers.ModelSerializer) :  
    class Meta: 
        model = Comments 
        fields = "__all__"


class BlogSerializers(serializers.ModelSerializer) : 
    comments = CommentSerializers(many=True, read_only = True)
    class Meta:
        model = Blog
        fields = "__all__"