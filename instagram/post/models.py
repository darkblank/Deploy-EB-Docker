from django.conf import settings
from django.db import models

from member.models import User


class PostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(author=None)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               blank=True,
                               null=True,
                               on_delete=models.SET_NULL,
                               )
    photo = models.ImageField(upload_to='post')
    created_at = models.DateTimeField(auto_now_add=True)

    objects = PostManager()

    class Meta:
        ordering = ['-created_at']

        # def __str__(self):
        #     return self.pk


class PostComment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               blank=True,
                               null=True,
                               on_delete=models.SET_NULL,
                               )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
