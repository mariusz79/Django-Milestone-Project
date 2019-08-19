from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Donation(models.Model):
    sponsor = models.ForeignKey(User, default=1)
    amount = models.IntegerField(blank=False)
    paid_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return f'{self.sponsor.username} Donation {self.amount}'