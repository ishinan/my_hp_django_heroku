from django.shortcuts import render
import os
from home.views import ( 
    _get_current_year, 
    _read_md_file,
    _create_page_list,
)

# Create your views here.
def blog(request):
    copyright_year = _get_current_year()
    list_blog_pages = [ page for page in _create_page_list(content_dir='blog/content/blog', content_type='md') ]
    list_blog_metadata = _create_blog_metadata_list(blog_page_list=list_blog_pages)
    context = { 
        'blog_sections': list_blog_metadata,
        'copyright_year': copyright_year,
    }
    return render(request, 'blog/blog.html', context)


def blog_detail(request, pk):
    copyright_year = _get_current_year()
    list_blog_pages = [ page for page in _create_page_list(content_dir='blog/content/blog', content_type='md') ]
    list_blog_metadata = _create_blog_metadata_list(blog_page_list=list_blog_pages)
    context = { 
        'blog_sections': list_blog_metadata,
        'copyright_year': copyright_year,
    }
    return render(request, 'blog/blog_detail.html', context)


def _create_blog_metadata_list(blog_page_list=[]):
    '''
    Create a list which contains each blog's metadata by reading each blog page md file

    parameters:
        blog_page_list: a list of blog pages
    return:
        list of metadata of blog pages
    '''
    list_blog_metadata = []
    if len(blog_page_list) > 0:
        for blog_page in blog_page_list:
            _, meta_data = _read_md_file(blog_page['content_path'])
            meta_data['html_name'] = blog_page['html_name']
            list_blog_metadata.append(meta_data)

    if  len(list_blog_metadata) > 0:
        list_blog_metadata = sorted(list_blog_metadata , key=lambda x: int(x['html_name'].replace(".html", "")), reverse=True )
    return list_blog_metadata 