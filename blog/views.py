from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def blogs(request):
    #return HttpResponse('<h1>Blogs</h1>')
    context = {}
    return render(request, 'home/base.html', context)