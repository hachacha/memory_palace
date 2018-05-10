from django.contrib import admin

from .models import Room, Image, Image_Style, Words, Words_Style, Marquee_Style
# Register your models here.


admin.site.register(Image)
admin.site.register(Room)
admin.site.register(Words)
admin.site.register(Image_Style)
admin.site.register(Words_Style)
admin.site.register(Marquee_Style)