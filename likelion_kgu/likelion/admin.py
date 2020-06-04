from django.contrib import admin
from .models import likelion

# Register your models here.
class likelionAdmin(admin.ModelAdmin):
    list_display = ['id', 'group_number', 'programming_lang']
    list_display_links = ['id', 'group_number']

admin.site.register(likelion, likelionAdmin)