from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from parkingapp.models import User 
from parkingapp.models import Reservation
from parkingapp.models import Parkingspace
from parkingapp.models import Review
from parkingapp.serializers import UserModelSerializer
from parkingapp.serializers import ReservationModelSerializer
from parkingapp.serializers import ParkingspaceModelSerializer
from parkingapp.serializers import ReviewModelSerializer
'''class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
class ReservationViewset(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class=ReservationModelSerializer
class ParkingspaceViewset(ModelViewSet):
    queryset= Parkingspace.objects.all()
    serializer_class= ParkingspaceModelSerializer
class ReviewViewset(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer'''


# example to create list in views 
'''class Model1ListCreate(generics.ListCreateAPIView):
    queryset = Model1.objects.all()
    serializer_class = Model1Serializer'''
# Create your views here.

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
class ReservationListCreate(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class=ReservationModelSerializer
class ParkingspaceListCreate(generics.ListCreateAPIView):
      queryset= Parkingspace.objects.all()
      serializer_class= ParkingspaceModelSerializer
class ReviewListCreate(generics.ListCreateAPIView):
     queryset = Review.objects.all()
     serializer_class = ReviewModelSerializer
     


    