from django.urls import path
from contact_me import views


urlpatterns = [
    path('', views.contact_me),
]