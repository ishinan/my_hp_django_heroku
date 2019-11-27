from django.shortcuts import render, redirect
from home.views import _get_current_year, _read_md_file
import os
import requests
from dotenv import load_dotenv
from homepage.settings import BASE_DIR

load_dotenv(os.path.join(BASE_DIR, '.env'))

active_page = 'contact_me:contact_me'


# Create your views here.
def contact_me(request):
    copyright_year = _get_current_year()
    meta_data = {}
    content, meta_data = _read_md_file('contact_me/content/contact.md')
    context = { 
         'active_page': active_page,
         'copyright_year': copyright_year,
         'title': meta_data['title'][0],
        }
    return render(request, 'contact_me/contact.html', context)


def send_email(request):
    to_name = request.POST['name']
    to_email = request.POST['email']
    message = request.POST['message']
    to_name_email = [ f"{to_name} <{to_email}>" ]

    response = _send_simple_message(to_list=to_name_email, message=message )
    print(f"Mailgun: Status: {response.status_code} ")
    print(f"Mailgun: Body: {response.text} ")

    return redirect("/contact-me")


def _send_simple_message(to_list=[], subject=None, message="" ):
    MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY')
    MAILGUN_DOMAIN = os.getenv('MAILGUN_DOMAIN') 
    MY_EMAIL = os.getenv('MY_EMAIL') 

    sender_email_name = "MasaMasa"
    from_email = f"{sender_email_name} <postmaster@{MAILGUN_DOMAIN}>"
    to_list_emails = [ MY_EMAIL ] + to_list
    subject = message if message else f"Message from my heroku websiste: contact me"
    text = f"{message}"

    return requests.post(
            f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
            auth=("api", MAILGUN_API_KEY),
            data={"from": from_email,
                    "to": to_list_emails,
                    "subject": subject,
                    "text": text,
                },
        )
