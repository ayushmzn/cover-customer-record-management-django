from django.db import models
from django.contrib.auth.models import User
class user_info(models.Model):
    user_id = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.DateField()
    mobile = models.IntegerField()
class add_customer(models.Model):
    name = models.CharField(max_length=40)
    shop_name = models.CharField(max_length=100)
    cus_mobile = models.IntegerField()
    city = models.CharField(max_length=50 ,null=True,blank=True)
    address = models.TextField()
    doc = models.DateField()
class customer_transections(models.Model):
    customer_shop_name = models.CharField(max_length=100, null=True,blank=True)
    customer_id = models.IntegerField(null=True, blank=True)
    items = models.TextField(null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    rate = models.FloatField(null=True,blank=True)
    date_of_send_goods = models.DateField(null=True,blank=True)
    date_of_cr = models.DateField(null=True,blank=True)
    amount_of_goods = models.FloatField(null=True,blank=True)
    cr_amount = models.FloatField(null=True,blank=True)
