from django.urls import path
from .views import TaskListView, TaskDetailView, create_task, mark_task_completed

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/new/', create_task, name='create_task'),
    path('task/<int:pk>/complete/', mark_task_completed, name='mark_task_completed'),
]