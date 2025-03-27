from django.forms import ModelForm
from .models import details

class group(ModelForm):
    class Meta:
        model =details
        fields='__all__'
