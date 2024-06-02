from rest_framework import serializers
from .models import User
from .models import Reservation
from .models import Parkingspace
from .models import Review
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
class ReservationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
class ParkingspaceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parkingspace
        fields = "__all__"
class ReviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
    