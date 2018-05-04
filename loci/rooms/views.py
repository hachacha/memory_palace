from django.http import Http404
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from rooms.models import Room, Image, Image_Room_Style, Words, Words_Room_Style
from loci.settings import DERIVE_SET 

from random import randint

def clear_session(request):
	del request.session['derive']
	del request.session['derive_path']


	return HttpResponse('all clear capn')

def room_middleware(request):
	# sesh = request.session

	if 'derive' not in request.session:
	# if  sesh['derive'] == None:
		#get length of derive_set and put that in there.
		derive = randint(0,(len(DERIVE_SET)-1))
		request.session['derive'] = derive
		request.session['derive_path']  = DERIVE_SET[ derive ]

def index(request):
	room_middleware(request)

	return render(request,'index.html')
	# return HttpResponse("go to specific room jesus. this should redirect.")

def detail(request, room_id):
	# template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
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
