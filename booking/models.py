from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    """
    Represents a booking made by a user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(default="default@example.com")
    date = models.DateField(default=timezone.now)
    time = models.TimeField()
    guests = models.PositiveIntegerField(default=2)


def __str__(self):
    """
    String representation of the Booking model.
    """
    return (
        f"{self.name} - {self.date} at "
        f"{self.time} ({self.guests} guests)"
    )
