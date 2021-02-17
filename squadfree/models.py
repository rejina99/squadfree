from django.db import models

class Item(models.Model):

    video = models.CharField(max_length=2500)
    title = models.CharField(max_length=100)
    desc = models.TextField()


class Details(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField
    subject = models.TextField()
    message = models.CharField(max_length=500)
    def __str__(self):
        return self.name




