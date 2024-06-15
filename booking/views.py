from rest_framework import viewsets
from models import Booking, Room, Availability
from serializers import BookingSerializers, RoomSerializers, AvailabilitySerializers
from django.shortcuts import render, redirect 
from django.views import View
from .forms import BookingFrom

class BookingFromView(View):
    def get(self, request):
        form = BookingForm()
        return render(request, 'booking/booking_from.html', {'form': form})
    
    def post(self, request):
        from = BookingForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'booking/booking_from.html', {'form': form})


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializers_class = RoomSerializers

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializers_class = BookingSerializers

class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializers_class = AvailabilitySerializers