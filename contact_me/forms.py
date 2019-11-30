from django import forms
from .models import ContactMeMessage

class ContactMeForm(forms.ModelForm):

    class Meta:
        model = ContactMeMessage
        fields = ( 'name', 'email', 'message', )
        widgets = {
            'message': forms.Textarea(attrs={'cols': 80, 'rows': 4}),
        }