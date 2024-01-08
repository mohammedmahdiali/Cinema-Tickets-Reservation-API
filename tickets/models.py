from django.db import models

# Create your models here.

# Guest - Movie - Reservation

class Movie(models.Model):
    hall = models.CharField(max_length=10)
    moive = models.CharField(max_length=15)
    date = models.DateField()

class Guest(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=16)

class Reservation(models.Model):
    movie = models.ForeignKey(Movie, related_name='reservation_movie', on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, related_name='reservation_guest', on_delete=models.CASCADE)