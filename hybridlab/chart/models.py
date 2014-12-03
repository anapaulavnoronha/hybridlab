from django.db import models
from datetime import datetime 
# Create your models here.
class Simulation(models.Model):

	id = models.AutoField(primary_key=True)
	date = models.DateTimeField('pub date')
	inclination = models.DecimalField(max_digits=8,decimal_places=2)
	powerLoss = models.DecimalField(max_digits=8,decimal_places=2)
	fk_car_id = models.ForeignKey('Car', db_column='fk_car_id')
	

	def __str__(self):
		return self.pub_date.strftime('%d-%m-%Y %H:%M')

class Current(models.Model):
	id = models.AutoField(primary_key=True)
	fk_simulation_id = models.ForeignKey(Simulation, db_column='fk_simulation_id')
	value = models.DecimalField(max_digits=8, decimal_places=2)
	time = models.IntegerField()

class Consumption(models.Model):
	id = models.AutoField(primary_key=True)
	fk_simulation_id = models.ForeignKey(Simulation, db_column='fk_simulation_id')
	value = models.DecimalField(max_digits=8,decimal_places=2)
	time = models.IntegerField()

class Car(models.Model):
	id = models.AutoField(primary_key=True)
	model = models.CharField(max_length=50)
	mass = models.DecimalField(max_digits=8,decimal_places=2)
	dragCoefficient = models.DecimalField(max_digits=8,decimal_places=2)
	power = models.DecimalField(max_digits=8,decimal_places=2)
	frontalArea = models.DecimalField(max_digits=8,decimal_places=2)












