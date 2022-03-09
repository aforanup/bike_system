from django.forms import ModelForm
from . models import BikeModel, BikeImageModel


class BikeForm(ModelForm):
    class Meta:
        model = BikeModel
        fields = ['name', 'image']


class BikeForm(ModelForm):
    class Meta:
        model = BikeImageModel
        exclude = ['bike']
