from django.http import JsonResponse, response
from django.shortcuts import render

from .models import Guest, Reservation, Movie
from .serializers import GuestSerializer, MovieSerializer, ReservationSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins, status, filters, viewsets

def without_rest(request):
    guests = Guest.objects.all()
    list_of_dicts = list(guests.values())

    return JsonResponse(list_of_dicts, safe=False)

# FBV FUNCTION BASED VIEWS
@api_view(['GET', 'POST'])
def fbv(request):
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

@api_view(['GET', 'PUT', 'DELETE'])
def fbv_pk(request, pk):
    try:
        if request.method == 'GET':
            guest = Guest.objects.get(pk=pk)
            serializer = GuestSerializer(guest)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            guest = Guest.objects.get(pk=pk)
            serializer = GuestSerializer(guest, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            guest = Guest.objects.get(pk=pk)
            guest.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

# CBV CLASS BASED VIEWS
class GuestView(APIView):
    def get(self, request):
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)

class GuestView_pk(APIView):
    def get(self, request, pk):
        guest = Guest.objects.get(pk=pk)
        serializer = GuestSerializer(guest)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            guest = Guest.objects.get(pk=pk)
            serializer = GuestSerializer(guest, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Guest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        try:
            guest = Guest.objects.get(pk=pk)
            guest.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Guest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
# MIXIN METHOD
class MixinsList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class Mixins_pk( mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
    
# GENERIC METHOD 
class GenericList(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class GenericList_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

# ModelViewSet
class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

# FIND MOVIE
@api_view(['GET'])
def find_movie(request):
    movies = Movie.objects.filter(
        movie = request.GET.get('movie'),
        hall = request.GET.get('hall'))
    
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

# CREATE RESERVATION

@api_view(['POST'])
def create_reservation(request):
    movie = Movie.objects.filter(
        movie = request.GET.get('movie'),
        hall = request.GET.get('hall'))

    guest = Guest()
    guest.name = request.GET.get('name')
    guest.phone_number = request.GET.get('phone_number')
    guest.save()

    reservation = Reservation()
    reservation.movie = movie
    reservation.guest = guest
    reservation.save()

    return Response(status=status.HTTP_201_CREATED)