from rest_framework import mixins,generics

from django.shortcuts import render
from django.http import Http404, JsonResponse 
from apis.models import Students, Employess,Blog,Comments
from .serializers import StudentSerializers ,EmployeesSerializers, BlogSerializers,CommentSerializers
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Function Based Views
@api_view(['GET' ,'POST','DELETE'])
def studentsView(requests) : 
    # stu = { "name" : ["abhi" , "pael", 4] , "age" : [1,2,3]} 
    # age = stu["name"][0]  
    # stu = Students.objects.all() 
    # student_list = list(stu.values()) 

    if requests.method == 'GET':
        stu = Students.objects.all()  
        serial = StudentSerializers(stu, many=True)
        return Response(serial.data , status=status.HTTP_200_OK)
     

# Class Based Views 

class Employees(APIView): 
    def get(self, request):
        emp = Employess.objects.all() 
        serial = EmployeesSerializers(emp,many = True) 
        return Response(serial.data ,status=status.HTTP_200_OK)
   
    def post(self,request):
        serial = EmployeesSerializers(data=request.data) 
        if serial.is_valid() : 
            serial.save() 
            return Response(serial.data ,status=status.HTTP_201_CREATED) 
        return Response(serial.errors , status=status.HTTP_400_BAD_REQUEST)  
    

class  EmployeesDetailsViews(APIView):
    def get_object(self,pk): 
        try : 
            emplo = Employess.objects.get(pk=pk)  
            return emplo
        except Employess.DoesNotExist:
            raise Http404  
        
    def get(self ,request,pk) : 
        emp =self.get_object(pk) 
        serial = EmployeesSerializers(emp) 
        return Response(serial.data, status=status.HTTP_200_OK)   
    
    def put(self,request,pk): 
        emp = self.get_object(pk)  
        serial = EmployeesSerializers(emp, data = request.data)   
        if serial.is_valid() : 
            serial.save() 
            return Response(serial.data,status=status.HTTP_200_OK)  
        return Response(serial.errors , status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
    
        
    def delete(self,request,pk):
        emp = self.get_object(pk) 
        emp.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
class EmployeesMixin(mixins.ListModelMixin , mixins.CreateModelMixin ,generics.GenericAPIView) : 
    queryset = Employess.objects.all() 
    serializer_class = EmployeesSerializers 

    def get(self,request) : 
        return self.list(request)  
    def post(self,request) : 
        return self.create(request)

class EmployeesMixinDetails(mixins.RetrieveModelMixin ,mixins.UpdateModelMixin ,mixins.DestroyModelMixin, generics.GenericAPIView) :    
    queryset = Employess.objects.all() 
    serializer_class = EmployeesSerializers
    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request, pk) : 
        return self.update(request, pk)
   
    def delete(self,request,pk) :
        return self.destroy(request, pk)




class CommentsView(generics.ListCreateAPIView): 
    queryset = Comments.objects.all()  
    serializer_class = CommentSerializers


class BlogsView(generics.ListCreateAPIView) :
    queryset = Blog.objects.all()  
    serializer_class = BlogSerializers

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all() 
    serializer_class = BlogSerializers 
    lookup_field = 'pk' 


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all() 
    serializer_class = CommentSerializers 
    lookup_field = 'pk' 
    