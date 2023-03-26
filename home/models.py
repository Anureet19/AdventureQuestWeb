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


class GroupBook(models.Model):
    GROUP_PASS_CHOICES = [
        (0, 'Family'),
        (1, 'Student'),
        (2, 'Couple'),
    ]
    members = models.IntegerField(null=False, default=1, max_length=10),
    total_cost = models.DecimalField(max_digits=10, decimal_places=2),
    pass_type = models.IntegerField(null=False, max_length=1, choices=GROUP_PASS_CHOICES, default=0)
    number_of_pass = models.IntegerField(null=False, default=1)
    date = models.DateField(default=timezone.now)

    def total_package_cost(self):
        return self.members * 10

