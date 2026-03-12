from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_done', 'created_at')
    list_filter = ('is_done', 'created_at', 'user')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    list_editable = ('is_done',)
    date_hierarchy = 'created_at'

admin.site.register(Task, TaskAdmin)