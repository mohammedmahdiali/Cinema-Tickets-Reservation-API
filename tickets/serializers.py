from rest_framework import serializers
from .models import Guest, Movie, Reservation

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        # just for demo DON'T EXTRACT pk !!!
        # ديربالك
        fields = ['pk', 'reservation_guest', 'name', 'phone_number']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'