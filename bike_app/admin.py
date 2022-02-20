from django.contrib import admin
from . models import BikeModel, BikeImageModel, BikeDetailModel


admin.site.register(BikeModel)
admin.site.register(BikeDetailModel)
admin.site.register(BikeImageModel)
