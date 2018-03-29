# Setting models seems to be fucking hard

from django.db import models

from .tags import getTags

# Create your models here.

class Software(models.Model):
	title 		= models.CharField(max_length=20, null=False)
	short_descr = models.CharField(max_length=300, null=False)
	descr 		= models.CharField(max_length=600, null=False)
	version		= models.CharField(max_length=100, null=False, unique=True)
	category 	= models.CharField(max_length=200, null=False)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	isos 		= models.BooleanField(null=False)
	isRequested = models.BooleanField(null=False, default=False)
	requestedby = models.CharField(max_length=20, default="Admin")

	def __str__(self):
		res = self.title + ", Category : ["
		for x in self.category:
			res = res + x + " "
		res += "]"
		return res

class News(models.Model):
	title 		= models.CharField(max_length=20, null=False)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	short_descr = models.CharField(max_length=300, null=False)
	descr 		= models.CharField(max_length=600, null=False)

	def __str__(self):
		return self.title