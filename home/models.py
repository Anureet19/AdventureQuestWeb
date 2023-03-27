from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


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
    full_name = models.TextField(max_length=100, default="John Doe")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    entry_date = models.DateField(auto_now=False)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    number_of_people = models.PositiveIntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    price_paid = models.IntegerField(default=0)
    booking_id = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.full_name


class GroupBook(models.Model):
    GROUP_PASS_CHOICES = (
        (0, 'Family'),
        (1, 'Student'),
        (2, 'Couple'),
    )
    SUB_PASS_CHOICES = (
        (0, 'Silver Pass'),
        (1, 'Blue Pass'),
        (2, 'Gold Pass'),
    )
    members = models.IntegerField(null=False, default=1)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pass_type = models.IntegerField(null=False, max_length=1, choices=GROUP_PASS_CHOICES, default=0)
    sub_pass_type = models.IntegerField(null=False, max_length=1, choices=SUB_PASS_CHOICES, default=0)
    number_of_pass = models.IntegerField(null=False, default=1)
    date = models.DateField(default=timezone.now)
        

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
        return self.title
    
class Ride(models.Model):
    name = models.CharField(max_length=200)
    height_limit = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    duration = models.DurationField()

    def __str__(self):
        return self.name

