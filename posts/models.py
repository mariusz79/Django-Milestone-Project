from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    """
    A single blog post
    """

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to='img', blank=True, null=True)
    likes = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def class_name(self):
        return self.__class__.__name__


class Like(models.Model):
    """Upvoting Posts"""
    liker_user = models.ForeignKey(User, null=True)
    liked_post = models.ForeignKey(Post, null=True)


class Comment(models.Model):
    """Comments on post"""
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200, blank=True)
    text = models.TextField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        # sort comments in chronological order by default
        ordering = ('created_date',)

    def __str__(self):
        return self.text