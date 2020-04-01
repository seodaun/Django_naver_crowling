from django.db import models

# Create your models here.


class BoardData(models.Model):
    title = models.CharField(max_length=300)  
    lank = models.CharField(max_length=3)