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

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name' , 'due_date' , 'checked']

    name = forms.CharField(max_length=128 , widget=forms.TextInput(attrs={
        'type' : 'text',
        'id' : 'taskInput',
        'placeholder' : "Update task"
    }))

    due_date = forms.DateField(widget=forms.TextInput(attrs={
        'type' : 'date',
        'id' : 'dueDateInput'
    }))

    checked = forms.CheckboxInput()

    deleter = forms.CheckboxInput()

    def update(self , id):
        todo = Todo.objects.get(id = id)
        todo.name = self.cleaned_data['name']
        todo.checked = self.cleaned_data['checked']
        todo.due_date = self.cleaned_data['due_date']

        todo.save()
    @staticmethod
    def delete_entity(id):
        Todo.objects.get(id).delete()