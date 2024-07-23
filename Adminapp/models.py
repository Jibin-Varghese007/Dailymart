from django.db import models

# Create your models here.
class Dailycategory(models.Model):
 categoryName = models.CharField(max_length=20)
 categoryDescription = models.TextField()
 img = models.ImageField(upload_to= 'images', default='null.jpeg')

class Products(models.Model):
 ProductName = models.CharField(max_length=20)
 Price = models.IntegerField()
 Productcategory = models.CharField(max_length=20)
 img = models.ImageField(upload_to= 'image', default='null.jpeg')

