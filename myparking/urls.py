"""
URL configuration for myparking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from parkingapp import views
from parkingapp.views import UserListCreate
from parkingapp.views import ReservationListCreate
from parkingapp.views import ParkingspaceListCreate
from parkingapp.views import ReviewListCreate
'''from parkingapp.views import UserListCreate
from parkingapp.views import ReservationListCreate
from parkingapp.views import ParkingspaceListCreate
from parkingapp.views import ReviewListCreate'''



'''urlpatterns = [
    path('admin/', admin.site.urls),
    #path('/',include('parkingapp.urls')),
    path('apiuser',include(router.urls)),
    path('apireservation',include(router.urls)),
    path('apipakingspace',include(router.urls)),
    path('apireservation',include(router.urls)),
] '''
urlpatterns = [
      path('admin/', admin.site.urls),
      #path('api/',include('parkingapp.urls')),
      path('User/',UserListCreate.as_view()),
      path('Reservation/',ReservationListCreate.as_view()),
      path('parkingspace/',ParkingspaceListCreate.as_view()),
      path('review/',ReviewListCreate.as_view())

]