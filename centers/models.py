from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

class Center(models.Model):
    name = models.CharField(max_length=200, blank=False)
    # center_type line removed
    address = models.TextField(blank=False)
    city = models.CharField(max_length=100, blank=False)
    contact_number = models.CharField(
    max_length=15,
    blank=True,  # This makes it optional in the Admin form
    null=True,   # This allows the database to store a 'NULL' value
    validators=[RegexValidator(r'^\d{10}$', 'Contact number must be 10 digits')]
)
    # Latitude aur Longitude Maps par dikhane ke liye
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        validators=[MinValueValidator(-90), MaxValueValidator(90)]
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        validators=[MinValueValidator(-180), MaxValueValidator(180)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['city', 'name']

    def __str__(self):
        # Updated to remove the center_type call
        return f"{self.name} ({self.city})"