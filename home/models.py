from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tier(models.Model):
    name = models.CharField(max_length=30, default="Gold")
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Package(models.Model):
    PACKAGE_STATUS = (
        ("1", "Available"),
        ("2", "Not Available"),
    )

    PACKAGE_TYPE = (
        ("1", "Season"),
        ("2", "Monthly"),
        ("3", "Daily"),
    )

    package_type = models.CharField(max_length=50, choices=PACKAGE_TYPE)
    price_factor = models.IntegerField()
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE)
    status = models.CharField(choices=PACKAGE_STATUS, max_length=15)

    def __str__(self):
        return self.package_type


class Reservation(models.Model):
    entry_date = models.DateField(auto_now=False)
    expiry_date = models.DateField()
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_id = models.CharField(max_length=100, default="null")

    def __str__(self):
        return self.guest.username
