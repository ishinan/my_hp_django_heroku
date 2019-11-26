from django.shortcuts import render
import requests
from home.views import _get_current_year, _read_md_file

# Create your views here.
def get_repo(request):
    copyright_year = _get_current_year()
    response = requests.get('https://api.github.com/users/ishinan/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
        'copyright_year': copyright_year,
    }
    return render(request, 'api_github/github.html', context) 