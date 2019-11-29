from django import forms
from .models import ContactMeMessage

class ContactMeForm(forms.ModelForm):

    class Meta:
        model = ContactMeMessage
        fields = ( 'name', 'email', 'message', )

