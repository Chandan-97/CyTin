from django.db import models

# Create your models here.

class Software(models.Model):
	title 		= models.CharField(max_length=20, null=False)
	descr 		= models.CharField(max_length=600, null=False)
	short_descr = models.CharField(max_length=300, null=False)
	more_link	= models.CharField(max_length=100, null=False, unique=True)
	category 	= models.CharField(max_length=200, null=False)
	timestamp 	= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title