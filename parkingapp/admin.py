from django.contrib import admin
from .models import User
admin.site.register(User)
from .models import Reservation
admin.site.register(Reservation)
from .models import Parkingspace
admin.site.register(Parkingspace)
from .models import Review
admin.site.register(Review)

# Register your models here.
