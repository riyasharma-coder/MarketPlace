from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('giver', 'Giver'),
        ('receiver', 'Receiver'),
        ('community', 'Community Member'),
        ('ngo', 'NGO Partner'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='community')
    location = models.CharField(max_length=255, blank=True)
    sustainability_interests = models.TextField(blank=True)
    
    # Ye line add karein:
    profile_image = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg', blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"