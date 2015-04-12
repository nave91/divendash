from django.shortcuts import render
from django.core.urlresolvers import reverse

from django_twilio.decorators import twilio_view
from twilio.twiml import Response

from django.views.generic import View


# def is_verify(request):
# 	text = request.POST.get('Body', '').lower()
# 	if 'verify' in text:
# 		return True
# 	else:
# 		return False

@twilio_view
def sms(request):
	
	# if is_verify(request):
	# 	return Response(reverse('verify_view'))
    name = request.POST.get('Body', '')
    msg = 'Hey %s, how are you today?' % (name)
    r = Response()
    r.message(msg)
    return r


# class Verify(View):
# 	def post(request):
# 		msg = 'wow'
# 		r = Response()
# 	    r.message(msg)
# 	    return r

