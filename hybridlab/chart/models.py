from django.db import models

# Create your models here.
class Simulation(models.Model):
	id = models.IntegerField(primary_key=True)
	start_datetime = models.DateField()
	end_datetime = models.DateField()
	tension = models.CharField(max_length=50)
	fuel_consumption = models.CharField(max_length=50)







