from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'due_date', 'city']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'title': 'Título',
            'description': 'Descripción',
            'completed': 'Completado',
            'due_date': 'Fecha de vencimiento',
            'city': 'Ciudad',
        }
    
    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date < timezone.now().date():
            raise forms.ValidationError("La fecha de vencimiento no puede ser anterior a la fecha actual.")
        return due_date