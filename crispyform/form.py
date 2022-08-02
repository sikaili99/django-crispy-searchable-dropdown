from django.forms import ModelForm, Select
from .models import Car

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ('car_type',)
        widgets = {
            'car_type': Select(),
        }