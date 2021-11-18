from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def gowri(request):
    return HttpResponse('gowri is  avery good gilr')

def shivani(request):
    return render(request,'app1/h1.html')