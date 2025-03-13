from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Task
from .forms import TaskForm

class TaskListView(View):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'task_manager/task_list.html', {'tasks': tasks})

class TaskDetailView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'task_manager/task_detail.html', {'task': task})

class CreateTaskView(View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'task_manager/task_form.html', {'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, 'task_manager/task_form.html', {'form': form})

class MarkTaskCompletedView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.completed = True
        task.save()
        return redirect('task_detail', pk=pk)