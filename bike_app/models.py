from django.db import models
from django.contrib.auth.models import User


class BikeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="bike_image/", null=True, blank=True)

    class Meta:
        verbose_name = "Bike"
        verbose_name_plural = "Bikes"

    def __str__(self):
        return f'{self.name}'


class BikeDetailModel(models.Model):
    bike = models.OneToOneField(
        BikeModel, related_name="bike_model", on_delete=models.CASCADE
    )
    description = models.TextField()

    class Meta:
        verbose_name = "Bike Detail"
        verbose_name_plural = "Bike Details"

    def __str__(self):
        return f'{self.bike.name}'


class BikeImageModel(models.Model):
    bike = models.ForeignKey(
        BikeModel, related_name="bike_images", on_delete=models.CASCADE, blank=True, null=True
    )
    image = models.ImageField(upload_to='bike_image/')

    class Meta:
        verbose_name = "Bike Image"
        verbose_name_plural = "Bike Images"

    def __str__(self):
        return f'{self.bike.name}'
