from django.db import models

from people.models import Address

class Bar(models.Model):
	name = models.CharField(max_length=100)
	address = models.ForeignKey(Address)

