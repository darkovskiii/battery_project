from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='uploads/' ,blank = True, null = True)