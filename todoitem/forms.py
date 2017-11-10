from django import forms
from .models import TodoItem

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ('name', 'done')
        
#forms.py is just a django shortcut of creating a form so you dont have to fill up your index .html with a contact form.