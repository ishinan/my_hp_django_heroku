from django.shortcuts import render
import os
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
def _create_page_list(content_dir='content', content_type='md'):
    '''
    This is a generator.
    Read a list of content html files under a content directory
    Return a dict of content path, target path, title, html name(without html extention)
    
    An example of a dictionary:
    {
        'content_path': 'content/index.md',
        'file_name': 'index,
        'html_name': 'index.html',
    }

    parameters:
        content_dir: default: 'content'
        content_type: file exntension: .md or .html (default: md)
    return:
        a dictionary of 
            'content_path', 
            'file_name', 
            'html_name'
    '''
    for curr_dir, list_dirs, list_files in os.walk(content_dir):
        for content_file in filter(lambda fname: fname.endswith(content_type), list_files):
            content_path = os.path.join(curr_dir, content_file)
            content_file_name, ext = os.path.splitext(content_file)
            target_file_name = content_file_name + ".html"

            yield {
                    'content_path': content_path,
                    'file_name': content_file_name,
                    'html_name': target_file_name,
                  }


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
