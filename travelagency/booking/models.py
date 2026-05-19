from django.db import models
from django.contrib.auth.models import User




class TravelPackage(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    available_slots = models.IntegerField(default=10)


    def __str__(self):
        return self.name
    
class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    package = models.ForeignKey(TravelPackage, on_delete=models.CASCADE)
    booked_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.package.name}"