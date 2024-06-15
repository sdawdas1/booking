from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField(decimal_place=2)
    capacity = models.IntegerField()

def __str__(self):
    return self.name 

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    confirmed = models.BooleanField(default=False)


def __str__(self):
    return f'{self.user.username} - {self.room.name}'


class Availability(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateTimeField()
    availability = models.BooleanField(default=False)


def __str__(self):
    return f'{self.room.name} - {self.date} - {self.available}'