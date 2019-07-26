from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Goods(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]


class Comment(models.Model):
    comment = models.CharField(max_length=200, blank=True)
    pup_date = models.DateTimeField('date published', blank=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    goods = models.ForeignKey(
        Goods, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.comment
