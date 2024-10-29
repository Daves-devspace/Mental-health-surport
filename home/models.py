from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=255, blank=True)
    province = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=125, blank=True)

    def __str__(self):
        return self.user.username
#sessions -therapy
class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    duration = models.DurationField()  # e.g., 30 minutes
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Session for {self.user.username} on {self.date}"
#Resource model
class Resource(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Packages(models.Model):
    service =models.CharField(max_length=100)
    preview=models.TextField()
    Charges=models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return self.service
