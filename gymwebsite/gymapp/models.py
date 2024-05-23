from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Membershiptype(models.Model):
    type = models.CharField(max_length=50)
    image = models.ImageField(default='')
    plan_validity = models.CharField(max_length=50)
    price = models.CharField(max_length=10)


class Member(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    address = models.CharField(max_length=1000)
    membershipname = models.CharField(max_length=100,default='')
    timeslot = models.CharField(max_length=100,default='')
    validity = models.CharField(max_length=50,default='inactive')
    price = models.CharField(max_length=10,default='')
    join_date = models.DateField(auto_now_add=True)
    expire_date = models.DateField(default='')

class No_of_people(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    membershiptype = models.CharField(max_length=100,default='')
    time = models.CharField(max_length=100)
    noofpeople = models.IntegerField(default=0)

class Contact(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    name = models.CharField(max_length=100,default='')
    phone = models.CharField(max_length=15,default='')
    message = models.CharField(max_length=1000,default='')






        