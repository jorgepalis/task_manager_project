from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Task
from .forms import TaskForm
from .utils import get_weather

class TaskListView(View):
    def get(self, request):
        # Verificar si hay un parámetro 'completed' en la URL
        completed_filter = request.GET.get('completed', None)
        
        # Iniciar con todas las tareas
        tasks = Task.objects.all()
        
        # Filtrar si se especificó el parámetro 'completed'
        if completed_filter is not None and completed_filter not in ['', 'all']:
            # Convertir el valor a booleano
            is_completed = completed_filter.lower() in ['true', '1', 'yes', 'si', 'sí']
            tasks = tasks.filter(completed=is_completed)
        
        # Buscar por título/descripción si existe el parámetro 'search'
        search_query = request.GET.get('search', '')
        if search_query:
            from django.db.models import Q
            tasks = tasks.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
            
        return render(request, 'task_manager/task_list.html', {
            'tasks': tasks,
            'completed_filter': completed_filter,
            'search_query': search_query
        })
    
class Base(View):
    def get(self, request):
        return render(request, 'task_manager/base.html')

class TaskDetailView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        city = task.city
        data = get_weather(city)
        if data.get('success'):
            climate = {
                'temperatura': data['temperatura'],
                'descripcion': data['descripcion'],
                'humedad': data['humedad']
            }
            error = None
        else:
            climate = None
            error = data.get("error")

        return render(request, 'task_manager/task_detail.html', {'task': task, 'climate': climate, 'error': error})

class DeleteTaskView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'task_manager/task_confirm_delete.html', {'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('task_manager:task_list')
    

class UpdateTaskView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task)
        return render(request, 'task_manager/task_form.html', {'form': form, 'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_manager:task_list')
        return render(request, 'task_manager/task_form.html', {'form': form})

def create_task(request):
    """Vista basada en funciones para crear una nueva tarea."""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_manager:task_list')
    else:
        form = TaskForm()
    
    return render(request, 'task_manager/task_form.html', {'form': form})

def mark_task_completed(request, pk):
    """Vista basada en funciones para marcar una tarea como completada."""
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        if task.completed:
            task.completed = False
        else:
            task.completed = True  
        task.save()
        return redirect('task_manager:task_detail', pk=task.id)
    return redirect('task_manager:task_list')  

