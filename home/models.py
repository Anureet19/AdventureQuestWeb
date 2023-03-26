from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tier(models.Model):
    name = models.CharField(max_length=30, default="Gold")

    def __str__(self):
        return self.name


class Package(models.Model):
    PACKAGE_STATUS = (
        ("1", "Available"),
        ("2", "Not Available"),
    )

    PACKAGE_TYPE = (
        ("S", "Season"),
        ("M", "Monthly"),
        ("D", "Daily"),
    )
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE)
    package_type = models.CharField(max_length=50, choices=PACKAGE_TYPE)
    price = models.IntegerField()
    capacity = models.IntegerField()
    status = models.CharField(choices=PACKAGE_STATUS, max_length=15)

    def __str__(self):
        return f'{self.package_type} {self.tier}'


class Reservation(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    entry_date = models.DateField(auto_now=False)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    number_of_people = models.PositiveIntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])

    def __str__(self):
        return self.guest.username

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.full_name