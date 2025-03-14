from django.urls import path
from .views import TaskDetailView, TaskListView, create_task, mark_task_completed, Base, DeleteTaskView, UpdateTaskView

app_name = 'task_manager'

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('base/', Base.as_view()),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/new/', create_task, name='create_task'),
    path('task/<int:pk>/complete/', mark_task_completed, name='mark_task_completed'),
    path('task/<int:pk>/delete/', DeleteTaskView.as_view(), name='delete_task'),
    path('task/<int:pk>/edit/', UpdateTaskView.as_view(), name='edit_task'),
]