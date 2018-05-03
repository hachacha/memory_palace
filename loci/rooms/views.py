from django.http import Http404
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from rooms.models import Room, Image, Image_Room_Style, Words, Words_Room_Style

def index(request):
	return HttpResponse("Hello, world. You're at the rooms.")

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
