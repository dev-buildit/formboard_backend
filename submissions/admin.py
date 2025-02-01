from django.contrib import admin
from .models import CustomForm, FormSubmission

# Register your models here.
@admin.register(CustomForm)
class CustomFormAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at')
    search_fields = ('title', 'slug')
    prepopulated_fields = {"slug": ("title",)}

@admin.register(FormSubmission)
class FormSubmissionAdmin(admin.ModelAdmin):
    list_fields = ("form", "data", "submitted_at")