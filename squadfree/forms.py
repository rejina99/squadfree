from django import forms
from .models import Details

class ContactForm(forms.Form):
    class Meta:
        model = Details
        fields = '__all__'
