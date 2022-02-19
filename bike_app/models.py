from django.db import models


class BikeModel(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="bike_image/")

    class meta:
        verbose_name = "Bike"
        verbose_name_plural = "Bikes"

    def __str__(self):
        return self.name


class BikeDetailModel(models.Model):
    bike = models.OneToOneField(
        BikeModel, related_name="bike_model", on_delete=models.CASCADE
    )
    description = models.TextField()

    class meta:
        verbose_name = "Bike Detail"
        verbose_name_plural = "Bike Details"

    def __str__(self):
        return self.bike.name


class BikeImageModel(models.Model):
    bike_model = models.ForeignKey(
        BikeModel, related_name="bike_images", on_delete=models.CASCADE, blank=True
    )
    image = models.ImageField(upload_to='bike_image/')

    class meta:
        verbose_name = "Bike Image"
        verbose_name_plural = "Bike Images"

    def __str__(self):
        return self.bike.name
