from django.shortcuts import render, redirect
from home.views import _get_current_year, _read_md_file
import os
import requests
from dotenv import load_dotenv
from homepage.settings import BASE_DIR
from .forms import ContactMeForm


load_dotenv(os.path.join(BASE_DIR, '.env'))

active_page = 'contact_me:contact_me'


# Create your views here.
def contact_me(request):
    copyright_year = _get_current_year()
    meta_data = {}
    _, meta_data = _read_md_file('contact_me/content/contact.md')
    context = { 
         'active_page': active_page,
         'copyright_year': copyright_year,
         'title': meta_data['title'][0],
        }

    if request.method == "POST":
        form = ContactMeForm(request.POST)

        # 1. Save it to the database
        if form.is_valid():
            form.save(commit=True)
            print(f"1. Saved to database")
            print(f"-------------------------------")

        # 2. Send the message to me
        user_name = request.POST['name']
        user_email = request.POST['email']
        user_message = request.POST['message']
        user_name_email = [ f"{user_name} <{user_email}>" ]
        user_email_message = f"""
        Sender: {user_name_email[0]}
        Message: {user_message}
        """
        response_of_sending_to_me = _send_simple_message(message=user_email_message )
        print(f"2.1 Mailgun: Status: {response_of_sending_to_me.status_code} ")
        print(f"2.2 Mailgun: Body: {response_of_sending_to_me.text} ")
        print(f"-------------------------------")

        # 3. Send a thank-you message to the user
        my_name = os.getenv('MY_NAME') 
        message_to_user = f"""
        --- No Reply to this email ---
        Thank you for sending a mesage to me, {user_name}! 
        Hope you have a great day!

        Regards,
        {my_name}
        """
        response_of_sending_to_user = _send_simple_message(to_list=user_name_email, message=message_to_user)
        print(f"3.1 Mailgun: Status: {response_of_sending_to_user.status_code} ")
        print(f"3.2 Mailgun: Body: {response_of_sending_to_user.text} ")

        if response_of_sending_to_user.status_code == 200: 
            if response_of_sending_to_me.status_code == 200:
                context['content'] = f"<p2 style='color: blue'>Thank you! The email is on the way!</h2>"
            else:
                context['content'] = f"<p2 style='color: green'>Done. But, you may not receive a confirmation emai. Sorry.</h2>"
        else:
            context['content'] = f"<p2 style='color: read'>Sorry, my mail server failed.</h2>"

    form = ContactMeForm()
    context['form'] = form
    
    return render(request, 'contact_me/contact.html', context)


def _send_simple_message(to_list=[], sender_email=None, subject=None, message="" ):
    MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY')
    MAILGUN_DOMAIN = os.getenv('MAILGUN_DOMAIN') 
    MY_EMAIL = os.getenv('MY_EMAIL') 

    # Sender
    if sender_email:
        from_email = sender_email 
    else:
        sender_email_name = "Masa Yana"
        from_email = f"{sender_email_name} <mailgun@{MAILGUN_DOMAIN}>"

    # Recipients
    if len(to_list) > 0:
        to_list_emails = [ MY_EMAIL ] + to_list
    else:
        to_list_emails = [ MY_EMAIL ] 

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
