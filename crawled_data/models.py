from django.db import models

# Create your models here.


class BoardData(models.Model):
    title = models.CharField(max_length=300)  
    def __str__(self):
    	return self.title
