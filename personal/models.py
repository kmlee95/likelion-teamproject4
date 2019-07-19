from django.db import models

class Personal(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='images/', null = True)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]


    