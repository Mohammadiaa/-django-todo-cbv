from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View
# Create your views here.
class TaskListView(LoginRequiredMixin,ListView):
     model = Task
     template_name = "tasks/task_list.html"
     context_object_name = "tasks"

     def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
     
class ToggleTaskView(LoginRequiredMixin, View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.is_done = not task.is_done
        task.save()
        return redirect('tasks:task_list')
class CreateTaskView(TemplateView):
     template_name = "tasks/task_form.html"    

class EditTaskView(TemplateView):
     template_name = "tasks/task_form.html" 

class DeleteTaskView(TemplateView):
     template_name = "tasks/task_confirm_delete.html"