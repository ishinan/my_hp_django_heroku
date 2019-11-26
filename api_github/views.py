from django.shortcuts import render
import requests

# Create your views here.
def get_repo(request):
    response = requests.get('https://api.github.com/users/ishinan/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'api_github/github.html', context) 