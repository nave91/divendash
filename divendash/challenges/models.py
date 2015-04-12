from django.db import models

from bluecan.models import Bar

class Challenge(models.Model):
	name = models.CharField(max_length=100)
	bar = models.ForeignKey(Bar)
	question = models.CharField(max_length=300)
	answer = models.BooleanField(default=False)
