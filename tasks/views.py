from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class TaskListView(TemplateView):
     template_name = "tasks/task_list.html"