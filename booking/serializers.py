from rest_framework import serializers
from models import Booking, Room, Availability

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        friends = '__all__'


class BookingSerializers(Booking.ModelSerializer):
    class Meta:
        model = Booking
        friends = '__all__'
    

class AvabilabilitySerializers(Availability.ModelSerializer):
    class Meta:
        model = Availability
        friends = '__all__'