from django.forms import ModelForm
from . models import BikeModel, BikeImageModel


class BikeForm(ModelForm):
    class Meta:
        model = BikeModel
        fields = ['name', 'image', 'description']


class BikeImageForm(ModelForm):
    class Meta:
        model = BikeImageModel
        fields = ['image']
