from django.db import models

class Center(models.Model):
    CENTER_TYPES = [
        ('e_waste', 'E-Waste Recycler'),
        ('cloth_bank', 'Cloth Bank'),
        ('ngo', 'NGO / Donation Center'),
    ]

    name = models.CharField(max_length=200)
    center_type = models.CharField(max_length=20, choices=CENTER_TYPES)
    address = models.TextField()
    city = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    # Latitude aur Longitude Maps par dikhane ke liye
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"{self.name} ({self.get_center_type_display()})"
    
