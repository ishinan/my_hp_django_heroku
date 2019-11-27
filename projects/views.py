from django.shortcuts import render
from home.views import _get_current_year, _read_md_file

active_page = 'projects:projects'

# Create your views here.
def projects(request):
    copyright_year = _get_current_year()
    context = {
        'active_page': active_page,
        'copyright_year': copyright_year,
    }
    return render(request, 'projects/projects.html', context)