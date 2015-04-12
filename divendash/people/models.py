from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext as _
from localflavor.us.models import USStateField

class Member(models.Model):
	name = models.CharField(max_length=100)
	phone = models.IntegerField(_("phone"), blank=True)

	def __str__(self):
		return str(name)+str(phone)

class Address(models.Model):
    address_1 = models.CharField(_("address"), max_length=128)
    address_2 = models.CharField(_("address cont'd"), max_length=128, blank=True)
    city = models.CharField(_("city"), max_length=64, default="Chattanooga")
    state = USStateField(_("state"), default="TN")
    zip_code = models.CharField(_("zip code"), max_length=5, default="37402")	

class Team(models.Model):
	name = models.CharField(max_length=100, default='badass')
	members = models.ForeignKey(Member)