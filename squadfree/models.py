from django.db import models

class Item(models.Model):

    video = models.CharField(max_length=2500)

