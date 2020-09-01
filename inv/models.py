from django.db import models

# Create your models here.

class Device(models.Model):

	typee = models.CharField(max_length=100, blank=True)
	price = models.IntegerField()

	choices = (
			('AVAILABLE', 'Item ready to be purchased'),
			('SOLD', 'Item Sold'),
			('RESTOCKING', 'Item restocking in few days')

		)
	status = models.CharField(max_length=100,choices=choices, default="SOLD")
	issues = models.CharField(max_length=100, default="No issues")

	class Meta:
		abstract = True
			

	def __str__(self):
		return 'Typee : {0} Price : {1}'.format(self.typee, self.price)

class laptop(Device):
	pass

class Desktop(Device):
	pass

class Mobile(Device):
	pass
