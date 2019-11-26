from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def home(request):
    #return HttpResponse('<h1>Home</h1>')
    copyright_year = _get_current_year()
    context = { 'copyright_year': copyright_year  }
    return render(request, 'home/base.html', context)


# Helpers
def _get_current_datetime():
    '''
    Get date/time info(year, month, date, hour, min) from datetime module

    return:
        datetime dictionary of year, month, date, hour, minute 
    '''
    now = datetime.datetime.now()
    return { 'year': now.strftime('%Y'), 
             'month': now.strftime('%m'),
             'date': now.strftime('%d'),
             'hour': now.strftime('%H'),
             'minute': now.strftime('%M')
            }

def _get_current_year():
    '''
    Get the current year

    return:
        current_year as integer
    '''
    d = _get_current_datetime()
    return d['year']
