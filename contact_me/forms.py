from django import forms
from .models import ContactMeMessage

class ContactMeForm(forms.ModelForm):

    class Meta:
        model = ContactMeMessage
        fields = ( 'name', 'email', 'message', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'rows': 4})