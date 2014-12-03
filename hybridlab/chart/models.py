from django.db import models
from datetime import datetime 
# Create your models here.
class Simulation(models.Model):

	id = models.IntegerField(primary_key=True)
	pub_date = models.DateTimeField('pub date', default=datetime.now)
	inclination = models.DecimalField(max_digits=8,decimal_places=2)
	id_car = models.ForeignKey('Car', db_column='id_car')
	powerLoss = models.DecimalField(max_digits=8,decimal_places=2)

	def __str__(self):
		return self.pub_date.strftime('%d-%m-%Y %H:%M')

class Current(models.Model):
	id = models.IntegerField(primary_key=True)
	id_simulation = models.ForeignKey(Simulation, db_column='id_simulation')
	current = models.IntegerField()
	time = models.IntegerField()

class Fuel(models.Model):
	id = models.IntegerField(primary_key=True)
	id_simulation = models.ForeignKey(Simulation, db_column='id_simulation')
	fuel = models.IntegerField()
	time = models.IntegerField()

class Car(models.Model):
	id = models.IntegerField(primary_key=True)
	carModel = models.CharField(max_length=50)
	mass = models.DecimalField(max_digits=8,decimal_places=2)
	dragCoeficient = models.DecimalField(max_digits=8,decimal_places=2)
	power = models.DecimalField(max_digits=8,decimal_places=2)
	frontalArea = models.DecimalField(max_digits=8,decimal_places=2)












