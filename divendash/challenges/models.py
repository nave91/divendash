from django.db import models

from bluecan.models import Bar



class Game(models.Model):
	name = models.CharField(max_length=10000)

	def __str__(self):
		return str(name)

class Challenge(models.Model):
	name = models.CharField(max_length=100)
	bar = models.ForeignKey(Bar)
	question = models.CharField(max_length=300)
	answer = models.BooleanField(default=False)
	game = models.ManyToManyField(Game)
