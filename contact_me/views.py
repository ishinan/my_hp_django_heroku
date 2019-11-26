from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contact_me(request):
    #return HttpResponse('<h1>Contact Me</h1>')
    context = {}
    return render(request, 'home/base.html', context)