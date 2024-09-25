from django import forms
from .models import ContactUsForm

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUsForm
        fields = ['name', 'email', 'message']

