from django.urls import path
from . import views
from .views import TaskListView,CreateTaskView,EditTaskView,DeleteTaskView

app_name = "tasks"

urlpatterns = [
    path("",TaskListView.as_view(), name="task_list"),
    path("create/",CreateTaskView.as_view(), name="create_task"),
    path("edit/<int:pk>/",EditTaskView.as_view(), name="edit_task"),
    path("delete/<int:pk>/",DeleteTaskView.as_view(), name="delete_task")
]
