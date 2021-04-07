from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request,data):
    return HttpResponse(f"<h1>Welcome to {data}</h1>")

def sample(request):
    return render(request,"sample1.html")

def temp1(request):
    return render(request,"sample3.html")
