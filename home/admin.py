from django.contrib import admin

# Register your models here.

from .models import Reservation, Tier, Package, Ride
# Register your models here.

admin.site.register(Reservation)
admin.site.register(Tier)
admin.site.register(Package)
admin.site.register(Ride)

