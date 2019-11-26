from django.urls import path
from api_github import views


urlpatterns = [
    path('', views.get_repo),
]