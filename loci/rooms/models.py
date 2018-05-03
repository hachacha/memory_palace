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

class Words_Room_Style(models.Model):
	room = models.ForeignKey('Room', on_delete=models.CASCADE)
	words = models.ForeignKey('Words', on_delete=models.CASCADE)
	color = models.CharField(max_length=7,default="#000000")

	class Meta:
		unique_together = ('room','words')

class Room(models.Model):
	images = models.ManyToManyField(Image, blank=True)
	text = models.ManyToManyField(Words, blank=True)
	created = models.DateTimeField('date published', auto_now_add=True)

class Static_Room(models.Model):
	title = models.CharField(max_length=300) 
	url = models.CharField(max_length=350)