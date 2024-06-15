from django import forms 
from .models import Booking


class BookingForm(form.ModelsForm):
    class Meta:
        model = Booking

    fields = ['user', 'room', 'start_date', 'end_date']