from django.urls import path
from api_github import views


app_name = 'api-github'

urlpatterns = [
    path('', views.get_repo, name='get_repo'),
]