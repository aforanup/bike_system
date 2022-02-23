from django.forms import ModelForm
from . models import BikeModel, BikeImageModel, BikeDetailModel


class BikeForm(ModelForm):
    class Meta:
        model = BikeModel
        fields = ['name', 'image']


class BikeDetailForm(ModelForm):
    class Meta:
        model = BikeDetailModel
        exclude = ['bike']


class BikeForm(ModelForm):
    class Meta:
        model = BikeImageModel
        exclude = ['bike']
