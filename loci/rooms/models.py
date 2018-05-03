from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.utils.crypto import get_random_string

# Create your models here.
class Image(models.Model):
	file = models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT), upload_to='images', default='settings.MEDIA_ROOT/images/')
	created = models.DateTimeField('date published')

	def __str__(self):
		return self.file.name	

class Words(models.Model):
	text = models.TextField()

	def __str__(self):
		return self.text

class Image_Room_Style(models.Model):
	room = models.ForeignKey('Room', on_delete=models.CASCADE)
	image = models.ForeignKey('Image', on_delete=models.CASCADE)
	width = models.IntegerField(default=0)
	height = models.IntegerField(defualt=0)
	border_radius = models.IntegerField(default=0)
	opacity = models.DecimalField(default=1.0)
	marquee = models.BooleanField(default=False)#should look this up...? maybe set up a function to do so.and automatically tie it to the IRS.

	class Meta:
		unique_together = ('room','image')

class Words_Room_Style(models.Model):
	room = models.ForeignKey('Room', on_delete=models.CASCADE)
	words = models.ForeignKey('Words', on_delete=models.CASCADE)
	color = models.CharField(max_length=7,default="#000000")


	class Meta:
		unique_together = ('room','words')

class Gen_Room_Style(models.Model):
	background_image = models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT), upload_to='images', default='settings.MEDIA_ROOT/images/')
	background_image_format = models.CharField(default='')

# class Div_Room_Style(models.Model):
# 	pass


class Marquee_Style(models.Model):
	image = models.ForeignKey('Image',on_delete=models.CASCADE, blank=True)
	words = models.ForeignKey('Words',on_delete=models.CASCADE, blank=True)

	behavior = models.CharField(max_length=24, default="scroll")
	direction = models.CharField(max_length=18,default="left")

class Room(models.Model):
	images = models.ManyToManyField(Image, blank=True)
	text = models.ManyToManyField(Words, blank=True)
	styles = models.ForeignKey(Gen_Room_Style, blank=True)
	created = models.DateTimeField('date published', auto_now_add=True)

class Static_Room(models.Model):
	title = models.CharField(max_length=300) 
	url = models.CharField(max_length=350)