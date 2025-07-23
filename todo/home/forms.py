from django import forms
from .models import Task


# Simple form to add tasks
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'due_date', 'category', 'done']

        widgets = {
            'due_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Select due date'
            }),
        }
