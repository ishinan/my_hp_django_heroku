from django.shortcuts import render
from django.http import HttpResponse
from home.views import _get_current_year, _read_md_file

# Create your views here.
def contact_me(request):
    #return HttpResponse('<h1>Contact Me</h1>')
    copyright_year = _get_current_year()
    meta_data = {}
    content, meta_data = _read_md_file('contact_me/content/contact.md')
    context = { 
                'copyright_year': copyright_year,
                'title': meta_data['title'][0],
              }
    return render(request, 'contact_me/contact.html', context)