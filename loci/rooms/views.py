from django.http import Http404
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from rooms.models import Room, Image, Image_Room_Style, Words, Words_Room_Style
from loci.settings import DERIVE_SET 

from random import randint

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
	if 'derive' not in request.COOKIES:
	# if  sesh['derive'] == None:
		#get length of derive_set and put that in there.
		derive = randint(0,(len(DERIVE_SET)-1))
		request.COOKIES['derive'] = derive
		request.COOKIES['derive_path']  = DERIVE_SET[ derive ]
		return True

def index(request):
	if room_middleware(request) is False:
		return HttpResponse('you must allow cookies')
	return render(request,'index.html')


def detail(request, room_id):
	
	try:
		room = Room.objects.get(pk=room_id)
		wrs = Words_Room_Style.objects.select_related('room')
		# w_styles = room.text.all()
		# print(w_styles)
	except Room.DoesNotExist:
		raise Http404("Room does not exist")
	return render(request, 'detail.html', {'room': room,'wrs':wrs})
	# template = loader.get_template('index.html')
	# context = {
	# 	'room_images_list' : 
	# }
 #    return HttpResponse(template.render(context, request))
	# return HttpResponse("hey you are in a particular room")
