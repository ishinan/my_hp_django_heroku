from django.shortcuts import render
from home.views import _get_current_year, _read_md_file

# Create your views here.
def projects(request):
    copyright_year = _get_current_year()
    context = {
        'copyright_year': copyright_year,
    }
    return render(request, 'projects/projects.html', context)