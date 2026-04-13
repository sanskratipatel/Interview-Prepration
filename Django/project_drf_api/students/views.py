from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def students(request):
    sud = [{'id' : {"he" : "ee"} , "name" : {"first_name" : "abhi" , "last_name" : "patel"}}] 
    first_name = sud[0]["name"]["first_name"]
    return HttpResponse(first_name)