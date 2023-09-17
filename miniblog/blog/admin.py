from django.contrib import admin
from .models import post

# Register your models here.

# we register post class here so that we can see our class model table in admin panel 
# we have created in models.py and list_display attributes used to display fields of tabel

@admin.register(post)

class PostModelAdmin(admin.ModelAdmin):
   list_display = ['id','title','description']