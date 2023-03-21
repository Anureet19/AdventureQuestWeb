from django.forms import ModelForm
from .models import Reservation


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['entry_date', 'package', 'guest']

