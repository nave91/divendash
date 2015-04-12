from django.test import TestCase
from django_dynamic_fixture import G

from django.contrib.auth.models import User, Group
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

class SmsViewTests(TestCase):

	def setUp(self):
		self.user = G(User)		
		self.account_sid = "AC3094732a3c49700934481addd5ce1659"
		self.auth_token  = "601cd75ed38da58f785a3caeb838d306"
		self.client = TwilioRestClient(self.account_sid, self.auth_token)
		import ipdb; ipdb.set_trace()
		self.sms = self.client.sms.messages.create(body="Wow me", to="+13049062914", from_="+15005550006")


	def test_hello(self):
		import ipdb; ipdb.set_trace()
		print hello