from django.contrib import admin

# Register your models here.
from .models import Room, Topik, Message

admin.site.register(Room)
admin.site.register(Topik)
admin.site.register(Message)