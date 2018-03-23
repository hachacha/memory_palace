from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rooms.models import Room, Image, Image_Room_Style, Words, Words_Room_Style

def index(request):
	return HttpResponse("Hello, world. You're at the rooms.")

def detail(request, room_id):
	return HttpResponse("hey you are in a particular room")
