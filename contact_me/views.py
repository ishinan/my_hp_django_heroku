from django.shortcuts import render, redirect
from home.views import _get_current_year, _read_md_file

active_page = 'contact_me:contact_me'

# Create your views here.
def contact_me(request):
    copyright_year = _get_current_year()
    meta_data = {}
    content, meta_data = _read_md_file('contact_me/content/contact.md')
    context = { 
         'active_page': active_page,
         'copyright_year': copyright_year,
         'title': meta_data['title'][0],
        }
    return render(request, 'contact_me/contact.html', context)


def send_email(request):
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']

    return redirect("/")