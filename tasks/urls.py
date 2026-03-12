from django.urls import path
from . import views
from .views import TaskListView,CreateFormView

app_name = "tasks"

urlpatterns = [
    path("",TaskListView.as_view(), name="task_list"),
    path("create/",CreateFormView.as_view(), name="create_task")
]
