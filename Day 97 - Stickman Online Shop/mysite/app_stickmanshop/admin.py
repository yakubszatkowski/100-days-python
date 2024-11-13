from django.contrib import admin
from .models import *

# Register your models here.
class SavedStickmanAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'stickman_name', 'stickman_clothes'] 

admin.site.register(SavedStickman, SavedStickmanAdmin)

