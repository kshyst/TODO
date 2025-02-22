from django import forms

from Todo.models import Todo


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name' , 'due_date']


    name = forms.CharField(max_length=128 , widget=forms.TextInput(attrs={
        'type' : 'text',
        'id' : 'taskInput',
        'placeholder' : "Add a new task!!!"
    }))

    due_date = forms.DateField(widget=forms.TextInput(attrs={
        'type' : 'date',
        'id' : 'dueDateInput'
    }))

#<input type="text" id="taskInput" placeholder="Add a new task...">
#<input type="date" id="dueDateInput">
