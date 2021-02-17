from django.forms import ModelForm
from .models import Details

class CustomerForm(ModelForm):
    class Meta:
        model = Details
        fields = '__all__'
