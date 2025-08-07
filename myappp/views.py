from django.shortcuts import render,HttpResponse as resp
from django.template import loader


def home(request):
    return render(request , 'index.html')

def about(request):
    return