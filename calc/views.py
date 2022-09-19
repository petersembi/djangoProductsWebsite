from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home (request):
    # return HttpResponse("hello world")

    return render(request, 'calc/home.html', {'name':'Navin'})
    # What we have passed above here is json data, or python list

def add (request):

    val1 = int(request.POST['num1'])
    val2 = int (request.POST['num2'])
    res = val1 + val2
    return render(request, 'calc/result.html', {'result':res})