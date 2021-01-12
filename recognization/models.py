from django.db import models

from recognization.utils import random_image_name


# Create your models here.
class OCR(models.Model):
    image = models.ImageField(upload_to=lambda instance, filename: random_image_name(filename))
    result = models.JSONField()
