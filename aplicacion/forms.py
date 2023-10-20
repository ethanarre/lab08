from django.forms import ModelForm
from .models import *

class PrestamoForm(ModelForm):
    class Meta:
        model = Prestamos
        fields = '__all__'