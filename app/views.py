from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def jyoo(request):
    return  HttpResponse('jyoo good girl')
