from django.http import Http404
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from rooms.models import Room, Image, Image_Room_Style, Words, Words_Style, Marquee_Style
from loci.settings import DERIVE_SET 

from random import randint
import datetime

def clear_session(request):
	request.session.flush()


	return HttpResponse('all clear capn')

def room_middleware(request):
	
	request.session.set_test_cookie()
	if request.session.test_cookie_worked():
		request.session.delete_test_cookie()
		# :)
	else:
		return False
	#set the derive cookie. 
	if 'derive' not in request:
		response = HttpResponse('here we go')
	# if  sesh['derive'] == None:
		#get length of derive_set and put that in there.
		derive = randint(0,(len(DERIVE_SET)-1))
		max_age = 365 * 24 * 60 * 60  # 10 years
		expires = datetime.datetime.now() + datetime.timedelta(seconds=max_age)
		response.set_signed_cookie(key='derive',value=derive, expires=expires.strftime("%a, %d-%b-%Y %H:%M:%S GMT"), max_age=max_age)
		response.set_signed_cookie(key='derive_path',value = ', '.join([str(x) for x in DERIVE_SET[ derive ]]), expires=expires.strftime("%a, %d-%b-%Y %H:%M:%S GMT"), max_age=max_age )
		return response

def index(request):
	response = room_middleware(request)
	if  response is False:
		return HttpResponse('you must allow cookies')

	# return render(request,'index.html')
	return response


def detail(request, room_iter):

	try:

		split_derive = request.get_signed_cookie('derive_path').split(',')

		the_room = split_derive[room_iter-1]
		room = Room.objects.get(pk=the_room)

		wrs = Words_Style.objects.select_related('words')
		marq = Marquee_Style.objects.select_related('words')
		# w_styles = room.text.all()
		# print(w_styles)
	except Room.DoesNotExist:
		raise Http404("Room does not exist")
	return render(request, 'detail.html', {'room': room,'wrs':wrs, 'marq':marq})
	# template = loader.get_template('index.html')
	# context = {
	# 	'room_images_list' : 
	# }
 #    return HttpResponse(template.render(context, request))
	# return HttpResponse("hey you are in a particular room")
