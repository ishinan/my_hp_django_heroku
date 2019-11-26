from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    #return HttpResponse('<h1>Home</h1>')
    context = {}
    return render(request, 'home/base.html', context)