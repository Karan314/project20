from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def ind(request,data):
    return HttpResponse(f"<h1>Welcome to {data}</h1>")

def sample(request):
    return render(request,"sample2.html")

def temp2(request):
    return render(request,"sample4.html")