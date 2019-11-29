from django.urls import path
from django.http import HttpResponseRedirect
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from home import views
from homepage import settings



app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    #path('/favicon', views.favicon, name='favicon'),
    # path('favicon.ico', lambda x: HttpResponseRedirect(settings.STATIC_URL+'favicon.ico'), name='favicon'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'), permanent=False), name="favicon")
    #google chrome favicon fix
]
