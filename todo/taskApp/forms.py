from django import forms
from django.forms import TextInput, CharField

from .models import *

class taskForm(forms.ModelForm):
    
    class Meta:
        model = taskModel
        fields = '__all__'
        widgets = {
            'task': TextInput(attrs={
                'class': "input-box",
                'placeholder' : 'Add a Task',
                }),
        }