from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.utils.crypto import get_random_string
from django.contrib.postgres.fields import IntegerRangeField, FloatRangeField
from psycopg2.extras import NumericRange
from django.contrib.postgres.validators import RangeMinValueValidator, RangeMaxValueValidator


class Image(models.Model):
	file = models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT), upload_to='images', default='settings.MEDIA_ROOT/images/')
	created = models.DateTimeField('date published')

	def __str__(self):
		return self.file.name	


class Image_Style(models.Model):
	image = models.ForeignKey('Image', on_delete=models.CASCADE)
	width = IntegerRangeField(default='(1, 101)',
								 blank=True,
								 validators=[
									RangeMinValueValidator(1), 
									RangeMaxValueValidator(100)
								]
				)
	height = IntegerRangeField(default='(1,101)',
								 blank=True,
								 validators=[
									RangeMinValueValidator(1), 
									RangeMaxValueValidator(100)
								]
				)
	border_radius_tl = IntegerRangeField(default='(1,101)',
								 blank=True,
								 validators=[
									RangeMinValueValidator(1), 
									RangeMaxValueValidator(100)
								]
					)
	border_radius_tr =IntegerRangeField(default='(1,101)',
								 blank=True,
								 validators=[
									RangeMinValueValidator(1), 
									RangeMaxValueValidator(100)
								]
					)
	border_radius_bl = IntegerRangeField(default='(1,101)',
								 blank=True,
								 validators=[
									RangeMinValueValidator(1), 
									RangeMaxValueValidator(100)
								]
					)
	border_radius_br = IntegerRangeField(default='(1,101)',
								 blank=True,
								 validators=[
									RangeMinValueValidator(1), 
									RangeMaxValueValidator(100)
								]
					)
	opacity = FloatRangeField(default='(0.1, 1.1)',
								 blank=True,
								 validators=[
									RangeMinValueValidator(0.1), 
									RangeMaxValueValidator(1.1)
								]
					)
	marquee = models.BooleanField(default=False)#should look this up...? maybe set up a function to do so.and automatically tie it to the IRS.


class Words(models.Model):
	text = models.TextField()

	def __str__(self):
		return self.text

	
class Words_Style(models.Model):
	words = models.ForeignKey('Words', on_delete=models.CASCADE)
	color = IntegerRangeField(default='(0, 255)',
								 blank=True,
								 validators=[
									RangeMinValueValidator(0), 
									RangeMaxValueValidator(255)
								]
					)
	size = IntegerRangeField(default='(1, 10)',
								 blank=True,
								 validators=[
									RangeMinValueValidator(1), 
									RangeMaxValueValidator(10)
								]
					)
	style = models.CharField(max_length=8, default='',blank=True)
	marquee = models.BooleanField(default=False)

class Gen_Room_Style(models.Model):
	background_image = models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT), upload_to='images', default='settings.MEDIA_ROOT/images/')
	background_image_format = models.CharField(max_length=16,default='')

# class Div_Room_Style(models.Model):
# 	pass

class Marquee_Style(models.Model):
	image = models.ForeignKey('Image',on_delete=models.CASCADE, blank=True, null=True)
	words = models.ForeignKey('Words',on_delete=models.CASCADE, blank=True, null=True)
	behavior = models.CharField(max_length=24, default="scroll")
	direction = models.CharField(max_length=18,default="left")
	scrollamount = IntegerRangeField(default='(1, 5)',
								 blank=True,
								 null=True,
								 validators=[
									RangeMinValueValidator(1), 
									RangeMaxValueValidator(5)
								]
					)
	scrolldelay = IntegerRangeField(default='(1, 5)',
								 blank=True,
								 null=True,
								 validators=[
									RangeMinValueValidator(1), 
									RangeMaxValueValidator(5)
								]
					)

class Room(models.Model):
	images = models.ManyToManyField(Image, blank=True)
	text = models.ManyToManyField(Words, blank=True)
	# styles = models.ForeignKey('Gen_Room_Style', on_delete=models.CASCADE, blank=True, default=None)
	created = models.DateTimeField('date published', auto_now_add=True)

class Static_Room(models.Model):
	title = models.CharField(max_length=300) 
	url = models.CharField(max_length=350)





class Image_Room_Style(models.Model):
	room = models.ForeignKey('Room', on_delete=models.CASCADE)
	image = models.ForeignKey('Image', on_delete=models.CASCADE)
	width = models.IntegerField(default=0)
	height = models.IntegerField(default=0)
	border_radius = models.IntegerField(default=0)
	opacity = models.DecimalField(decimal_places=2, max_digits=3, default=1.0)
	marquee = models.BooleanField(default=False)#should look this up...? maybe set up a function to do so.and automatically tie it to the IRS.

	class Meta:
		unique_together = ('room','image')

class Words_Room_Style(models.Model):
	room = models.ForeignKey('Room', on_delete=models.CASCADE)
	words = models.ForeignKey('Words', on_delete=models.CASCADE)
	color = models.CharField(max_length=7,default="#000000")
	size = models.IntegerField(default=1)#should be in EM
	style = models.CharField(max_length=8, default='')
	marquee = models.BooleanField(default=False)


	class Meta:
		unique_together = ('room','words')
