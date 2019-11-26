from django.shortcuts import render
import datetime
import markdown


# Create your views here.
def home(request):
    copyright_year = _get_current_year()
    meta_data = {}
    content, meta_data = _read_md_file('home/content/index.md')
    context = { 
                'copyright_year': copyright_year,
                'title': meta_data['title'][0],
                'content': content,
              }
    return render(request, 'home/index.html', context)


# Helpers
def _read_md_file(file_path):
    '''
    Read a md exntention file and return its content and metadata

    parameter: 
        file_path
    return: 
        a list of conetent and metadata dict 
            - Note that metadata value is a list
            - Example: 
                [ 'html string', 
                  { 'key': [ 'value', ], 
                    'key': [ 'value' ],
                  },
                ]
    '''
    if file_path.endswith('.md'):
        with open(file_path , 'r') as f:
            content_of_md_file = f.read()
            md = markdown.Markdown(extensions=['meta', 'fenced_code', 'codehilite'])
            html_of_md_file = md.convert(content_of_md_file)
            dict_of_md_meta_data = md.Meta
            return [ html_of_md_file, 
                     dict_of_md_meta_data,
                   ]

    return [ "Could not find a md file" + file_path, {}, ]



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
