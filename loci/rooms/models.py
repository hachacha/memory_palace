from django.db import models

# Create your models here.
class Image(models.Model):
	location = models.CharField(max_length=200)
	created = models.DateTimeField('date published')
	
	def __str__(self):
		return self.title

class Image_Room_Style(models.Model):
	room = models.ForeignKey('Room', on_delete=models.CASCADE)
	image = models.ForeignKey('Image', on_delete=models.CASCADE)
	width = models.IntegerField(default=0)

class Room(models.Model):
	images = models.ManyToManyField(Image)
	created = models.DateTimeField('date published')
	
	def __str__(self):
		return self.title