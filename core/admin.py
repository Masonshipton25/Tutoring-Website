from django.contrib import admin
from .models import Subject, Topic

# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "order")
    list_filter = ("subject",)
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("subject", "order")