from django.forms import ModelForm
from .models import *

class AddMessageForm(ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
