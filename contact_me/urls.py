from django.urls import path
from contact_me import views

app_name = 'contact_me'

urlpatterns = [
    path('', views.contact_me, name="contact_me" ),
    path('send-email', views.send_email, name="send_email" ),
]