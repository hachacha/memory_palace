from django.contrib import admin

from .models import Room, Image, Image_Room_Style, Words, Words_Room_Style
# Register your models here.


admin.site.register(Image)
admin.site.register(Room)
admin.site.register(Words)
admin.site.register(Image_Room_Style)
admin.site.register(Words_Room_Style)