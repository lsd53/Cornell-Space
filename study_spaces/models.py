from django.db import models

# Create your models here.

class Space(models.Model):
	space_name = models.CharField(max_length=100)
	space_location = models.CharField(max_length=100)
	space_capacity = models.IntegerField()
	space_occupation = models.IntegerField(default=0)
