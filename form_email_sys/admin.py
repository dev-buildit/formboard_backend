from django.contrib import admin
from .models import FormData

# Register your models here.
@admin.register('FromData')
class AdminFormData(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
    list_filter = ['-created-at']
