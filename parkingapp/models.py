
from django.db import models


class User(models.Model):
    name= models.CharField(max_length=30)
    userid = models.BigAutoField(primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=30)
class Reservation(models.Model):
    startime = models.TimeField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    parkingid = models.IntegerField(max_length=40)
    endtime =  models.TimeField()
    userid = models.ForeignKey('User',on_delete=models.CASCADE)
    def duration(self):
        return self.startime-self.endtime
class Parkingspace(models.Model):
    parkingid = models.BigAutoField(primary_key=True)
    location = models.CharField(max_length=50)
    capacity = models.FloatField(max_length=20)
    Rate = models.DecimalField(max_digits=5,decimal_places=2)
    availablestatus = models.BooleanField(default=True)
class Review(models.Model):
    date = models.DateField(auto_now_add=True)
    comment =models.CharField(max_length=40)
    reviewid = models.BigAutoField(primary_key=True)
    userid = models.ForeignKey('User',on_delete=models.CASCADE)
    parkingid = models.ForeignKey('Reservation',on_delete=models.CASCADE)