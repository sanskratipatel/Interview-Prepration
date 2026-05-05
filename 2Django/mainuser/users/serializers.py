from .models import User , Order ,Product,OrderItem 
from rest_framework import serializers 

class ProductSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Product 
        fields = "__all__"