from django.contrib import admin
from .models import Reservation, Tier, Package, Contact, Directions

# Register your models here.

admin.site.register(Reservation)
admin.site.register(Tier)
admin.site.register(Package)
admin.site.register(Contact)
admin.site.register(Directions)