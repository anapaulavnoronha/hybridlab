from django.db import models
from datetime import datetime 
# Create your models here.
class Simulation(models.Model):

	id = models.IntegerField(primary_key=True)
	pub_date = models.DateTimeField('pub date', default=datetime.now)
	angulation = models.IntegerField()
	speed = models.IntegerField()
	power = models.IntegerField()

	def __str__(self):
		return self.pub_date.strftime('%d-%m-%Y %H:%M')

class Tension(models.Model):
	id = models.IntegerField(primary_key=True)
	id_simulation = models.ForeignKey(Simulation, db_column='id_simulation')
	tension = models.IntegerField()
	time = models.IntegerField()

class Fuel(models.Model):
	id = models.IntegerField(primary_key=True)
	id_simulation = models.ForeignKey(Simulation, db_column='id_simulation')
	fuel = models.IntegerField()
	time = models.IntegerField()







