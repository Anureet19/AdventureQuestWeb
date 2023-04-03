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
    entry_date = models.DateField(auto_now=False)
    expiry_date = models.DateField()
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
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

class Directions(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
<<<<<<< Updated upstream
        return self.title
=======
        return self.title


class Ride(models.Model):
    name = models.CharField(max_length=200)
    height_limit = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    duration = models.DurationField()

    def __str__(self):
        return self.name


class Users(models.Model):
    username = models.CharField(max_length=30, unique=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    pass1 = models.CharField(max_length=20)
    pass2 = models.CharField(max_length=20)

    def __str__(self):
        return self.username
>>>>>>> Stashed changes
