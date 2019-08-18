from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = ResizedImageField(default='default.jpg', upload_to='profile_pics', size=[250, 250], crop=['middle', 'center'])
    bugs = models.IntegerField(default=0)
    features = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Profile'

   