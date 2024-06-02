'''from rest_framework import routers
from parkingapp.views import UserViewset
from parkingapp.views import  ReservationViewset
from parkingapp.views import ParkingspaceViewset
from parkingapp.views import ReviewViewset

router = routers.DefaultRouter()
router.register(r'parkingapp',UserViewset)
router.register(r'parkingapp',ReservationViewset)
router.register(r'parkingapp',ParkingspaceViewset)
router.register(r'parkingapp',ReviewViewset)'''

from django.urls import path
from .views import UserListCreate
from .views import ReservationListCreate
from .views import ParkingspaceListCreate
from .views import ReviewListCreate
urlpatterns =[
    path('User/',UserListCreate.as_view(),name = "User-list-create"),
    path('Reservation/',ReservationListCreate.as_view(),name = "Reservation-list-create"),
    path('Parkingspace/',ParkingspaceListCreate.as_view(),name = "Parkingspace-list-create"),
     path('Review/',ReviewListCreate.as_view(),name = "Review-list-create") 
]

