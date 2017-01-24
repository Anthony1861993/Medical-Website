from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible

from django.db import models

@python_2_unicode_compatible
class Patient(models.Model):
	id = models.IntegerField(primary_key = True)
	PSA = models.DecimalField(max_digits=4, decimal_places=1)
	prostate_vol = models.DecimalField(max_digits=4, decimal_places=1)
	lesion_size = models.DecimalField(max_digits=4, decimal_places=1)
	sector = models.IntegerField()
	PIRADS_score = models.IntegerField()
	GLEASON_score = models.IntegerField()
	def __str__(self):
		return str(self.id)

'''   
@python_2_unicode_compatible
class Sector(models.Model):
	id = models.IntegerField(primary_key = True)
	count = models.IntegerField()
	def __str__(self):
		return str(self.id)
'''