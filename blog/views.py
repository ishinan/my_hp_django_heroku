from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def blogs(request):
    context = { 'outputfile': 'blog.html' }
    return render(request, 'blog/blog_base.html', context)