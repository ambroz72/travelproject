from django.http import HttpResponse
from django.shortcuts import render
from . models import Place 

# Create your views here.

def home(request):
    p=Place.objects.all()

    return render(request,"index.html",{'result':p})

# def next_page(request):
#     return render(request,'next_page.html')

# def addition(request):
#     x=int(request.GET['no1'])
#     y=int(request.GET['no2'])
#     ans=x+y
#     return render(request,'result.html',{'result':ans})