from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class TaskListView(TemplateView):
     template_name = "tasks/task_list.html"

class CreateTaskView(TemplateView):
     template_name = "tasks/task_form.html"    

class EditTaskView(TemplateView):
     template_name = "tasks/task_form.html" 

class DeleteTaskView(TemplateView):
     template_name = "tasks/task_confirm_delete.html"