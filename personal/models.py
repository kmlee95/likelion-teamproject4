from django.db import models
from django.contrib.auth.models import User


class Personal(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', null=True)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
