from django.shortcuts import render
from django.core.urlresolvers import reverse

from django_twilio.decorators import twilio_view
from twilio.twiml import Response
from people.models import Member
from django.views.generic import View
from challenges.models import Game

def parser(text):
	text = text.lower()
	if 'play' in text: return 'pl'
	elif 'join' in text: return 'jo'
	elif 'start' in text: return 'st'
	else: 
		return None

def play(num, body):
	words = body.split()
	if 'as' in words:
		as_index =  words.index('as')
		mem_name = words[as_index+1]
	else:
		mem_name = 'rockstar'+str(Member.objects.count())
	mem, created = Member.objects.get_or_create(phone=int(num[-10:]),name=str(mem_name))
	game_name = mem_name+str(Game.objects.count())
	game, created = Game.objects.get_or_create(name=game_name)
	msg = "Great %s!, Your game id is %s. Reply 'start' to start game" % (mem_name, game_name)
	return msg

@twilio_view
def sms(request):
	if request.method == 'POST':
	    num = str(request.POST.get('From', '')) 
    	body = str(request.POST.get('Body', ''))
    	status = parser(body)
    	r = Response()
    	if status:
    		if status == 'pl':
    			msg = play(num, body)
    		else:
	    		msg = str(status)
    	else:
	    	msg = "Hey! Reply with 'play as <name>', to dive!"
    	r.message(msg)
    	return r

