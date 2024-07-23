from django.db import models
from Adminapp.models import*
# Create your models here.
class vegecontact(models.Model):
  ContactName =  models.CharField(max_length=20)
  ContactNumber =  models.IntegerField()
  EmailId = models.EmailField(null=True)
  Message = models.TextField(default='')

class Fruitregister(models.Model):
   UserName =  models.CharField(max_length=20)
   Password =  models.CharField(max_length=10)
   EmailId = models.EmailField(null=True)
   Phonenumber = models.IntegerField()


class Cart(models.Model):
   cartuser = models.ForeignKey(Fruitregister,on_delete=models.CASCADE)
   cartproduct = models.ForeignKey(Products,on_delete=models.CASCADE)
   quantity = models.IntegerField()
   total = models.IntegerField()
   status = models.IntegerField(default=0)


class Checkout(models.Model):
   usercheckout = models.ForeignKey(Fruitregister,on_delete=models.CASCADE)
   checkoutcart = models.ForeignKey(Cart,on_delete=models.CASCADE)
   address = models.CharField(max_length=20)
   city = models.CharField(max_length=20)
   country = models.CharField(max_length=20)
   postcode = models.CharField(max_length=20)