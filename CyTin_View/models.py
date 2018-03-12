# Setting models seems to be fucking hard

from django.db import models

# Create your models here.

class Software(models.Model):
	title 		= models.CharField(max_length=20, null=False)
	short_descr = models.CharField(max_length=300, null=False)
	descr 		= models.CharField(max_length=600, null=False)
	version		= models.CharField(max_length=100, null=False, unique=True)
	category 	= models.CharField(max_length=200, null=False)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	isOs 		= models.BooleanField(null=False)

	def __str__(self):
		return self.title

class News(models.Model):
	title 		= models.CharField(max_length=20, null=False)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	short_descr = models.CharField(max_length=300, null=False)
	descr 		= models.CharField(max_length=600, null=False)

	def __str__(self):
		return self.title
