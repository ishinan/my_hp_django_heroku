from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def projects(request):
    #return HttpResponse('<h1>Projects</h1>')
    context = {}
    return render(request, 'projects/base.html', context)