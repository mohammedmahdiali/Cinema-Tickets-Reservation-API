from django.http import JsonResponse, response
from django.shortcuts import render
from .models import Guest, Reservation, Movie
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GuestSerializer, MovieSerializer, ReservationSerializer
from rest_framework import status, filters
# Create your views here.

def without_rest(request):
    guests = Guest.objects.all()
    list_of_dicts = list(guests.values())

    return JsonResponse(list_of_dicts, safe=False)

@api_view(['GET', 'POST'])
def fbv_list(request):
    # GET
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.data,
                        status=status.HTTP_400_BAD_REQUEST)

# @api_view()
# def ss():
#     pass