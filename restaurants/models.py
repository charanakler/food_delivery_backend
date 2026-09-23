from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    image = models.ImageField(
        upload_to="restaurants/",
        blank=True,
        null=True
    )
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=0.0
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name