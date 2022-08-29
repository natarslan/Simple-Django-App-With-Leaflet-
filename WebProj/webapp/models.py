from django.contrib.gis.db import models
from django.core.serializers import serialize


# Create your models here.
class Modelclass(models.Model):
	#Id = models.IntegerField(primary_key=True)
	#date = models.DateTimeField()
	#depth = models.FloatField()
	#place = models.CharField(max_length=200) # long description f the location
	geom = models.PointField() # Longitude and Latitude
	magnitude =  models.FloatField()
	country = models.CharField(max_length=10) # two letter country codes

	
	@property
	def lat_lng(self):
		return list(getattr(self.geom, 'coords', [])[::-1] )


	def __str__(self):
		return str(self.country)

	# @property
	# def place(self):
	# 	return str(self.country)

	# @property
	# def location(self):
	# 	return str(self.geom)

	# @property
	# def popupContent(self):
	# 	return str(self.magnitude)
	# 	#return '{}'.format(self.magnitude)
	# 	# return 'Country: {} Magnitude: {} '.format(
	# 	# 	self.country,
	# 	# 	self.magnitude)

	# def serialize(self):
	# 	import json
	# 	json_dict = {}
	# 	json_dict['type'] = 'Feature'
	# 	json_dict['country'] = dict(name = self.country)
	# 	json_dict['geom'] = dict(geom = self.geom)
	# 	json_dict['magnitude'] = dict(magnitude = self.magnitude)
	# 	return(json.dumps(json_dict))
