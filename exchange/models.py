from django.db import models
from django.conf import settings

class Item(models.Model):
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('furniture', 'Furniture'),
        ('books', 'Books'),
        ('clothing', 'Clothing'),
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    # YE LINE ADD KI HAI:
    is_swapped = models.BooleanField(default=False) 

    def __str__(self):
        return self.title

class SwapRequest(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='requests')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, default='pending') # pending, accepted, rejected
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} wants {self.item.title}"
    