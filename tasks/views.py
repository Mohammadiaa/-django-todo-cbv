from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView,DetailView,DeleteView,UpdateView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from .forms import TaskForm
# Create your views here.
class TaskListView(LoginRequiredMixin,ListView):
     model = Task
     template_name = "tasks/task_list.html"
     context_object_name = "tasks"
     paginate_by = 5

     def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
     
class ToggleTaskView(LoginRequiredMixin, View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.is_done = not task.is_done
        task.save()
        return redirect('tasks:task_list')
    
class CreateTaskView(LoginRequiredMixin,CreateView):
     model = Task
     form_class = TaskForm
     template_name = "tasks/task_form.html"    
     success_url = "/tasks/"

     def form_valid(self, form):
          form.instance.user = self.request.user
          return super().form_valid(form)
         
class EditTaskView(LoginRequiredMixin,UpdateView):
     model = Task
     form_class = TaskForm  
     template_name = "tasks/task_form.html"    
     success_url = "/tasks/"
class TaskDetailView(LoginRequiredMixin,DetailView):
     model = Task
     template_name = 'tasks/task_detail.html'
     context_object_name = 'task'



class DeleteTaskView(LoginRequiredMixin,DeleteView):
     model = Task
     template_name = "tasks/task_confirm_delete.html"
     success_url = "/tasks/"