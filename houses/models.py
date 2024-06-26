from django.db import models

class House(models.Model):
    """Model Definition for Houses"""
    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(verbose_name="Price", help_text="Positive Numbers Only")
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(verbose_name="Pets Allowed?",default=False, help_text="Does house allow pets?")

    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name