from django.forms import ModelForm, TextInput

from .models import City


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ('name',)
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control bg-dark text-light border-danger',
                'type': 'text',
                'id': 'city',
                'name': 'city',
                'placeholder': 'Enter command'
            })
        }
