from django.db import models

# Create your models here.

# Guest - Movie - Reservation

class Movie(models.Model):
    hall = models.CharField(max_length=10)
    movie = models.CharField(max_length=15)
    date = models.DateField()

    def __str__(self):
        return self.movie

class Guest(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    movie = models.ForeignKey(Movie, related_name='reservation_movie', on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, related_name='reservation_guest', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.guest.name) + ":" + str(self.movie.movie)