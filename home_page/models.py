from django.db import models

# Create your models here.
class todo(models.Model):
    added_date = models.DateTimeField()
    text       = models.CharField(max_length = 200)