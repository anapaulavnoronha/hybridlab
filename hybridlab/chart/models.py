from django.db import models
from datetime import datetime 
# Create your models here.
class Simulation(models.Model):
	id = models.IntegerField(primary_key=True)
	pub_date = models.DateTimeField('pub date', default=datetime.now)
	tension = models.CharField(max_length=50)
	fuel_consumption = models.CharField(max_length=50)

	def __str__(self):
		return self.pub_date.strftime('%Y-%m-%d %H:%M')







