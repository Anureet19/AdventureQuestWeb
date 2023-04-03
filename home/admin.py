from django.contrib import admin
<<<<<<< Updated upstream
from .models import Reservation, Tier, Package, Contact, Directions
=======
from .models import Reservation, Tier, Package, Contact, Directions, Ride, GroupBook,Users
>>>>>>> Stashed changes

# Register your models here.

admin.site.register(Reservation)
admin.site.register(Tier)
admin.site.register(Package)
admin.site.register(Contact)
<<<<<<< Updated upstream
admin.site.register(Directions)
=======
admin.site.register(Directions)
admin.site.register(Ride)
admin.site.register(GroupBook)
admin.site.register(Users)
>>>>>>> Stashed changes
