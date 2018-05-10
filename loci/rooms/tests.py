from .models import Room, Words, Words_Room_Style, Words_Style, Image, Image_Room_Style, Image_Style
from django.test import TestCase
from django.db.utils import IntegrityError

# Create your tests here.
# class RoomsModelsTests(TestCase):

# 	def setUp(self):
# 		#just need to be testing words and room for now
# 		w = Words.objects.create(text="i am some test text")
# 		w.save()

# 		r = Room()
# 		r.save()
# 		r.text.add(w)


# 	def test_Unique_together_gives_validation_error_on_not_unique(self):
# 		wrs = Words_Room_Style()
# 		duplicate_wrs = Words_Room_Style()
		
# 		wrs.color="purple"
# 		wrs.room=Room.objects.get(pk=1)
# 		wrs.words=Words.objects.get(pk=1)
# 		wrs.save()
		
# 		duplicate_wrs.color="red"
# 		duplicate_wrs.room=Room.objects.get(pk=1)
# 		duplicate_wrs.words=Words.objects.get(pk=1)

# 		try:
# 			duplicate_wrs.save()
# 			print("integrity error did not fire")
# 			self.assertTrue(0)
# 		except IntegrityError:
# 			print("integrity error fired correctly")
# 			self.assertTrue(1)


class ImageModelsTests(TestCase):
	
	def setUp(self):
		i = Image.objects.create(file='/home/jon/Desktop/image_uploaded_from_ios.jpg')	
		w = Words.objects.create(text="i am some test text")
		ws = Words_Style.objects.create(words=w,color_r_int=10,color_range_r=(1,255),size=1)
		r = Room()
		r.save()
		r.text.add(w)
		r.images.add(i)
		r.save()

		print("setupcompleted")

	def test_returnNewColorOnWordsModel(self):
		#this is going to go to be the same if someone clicks on the words and changes the styling a bit. 
		#run function and expect the r to increase in color.
		pass
	def test_returnNewStyleOnImageModel(self):
		pass