from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, FileField, ClearableFileInput, TextInput, ChoiceField
from django.forms.widgets import HiddenInput, DateInput, Select
from .models import Task, Application


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ('text', 'price')


class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

        labels = {
            'username': 'Уникальное имя пользователя',
            'email': 'Адрес эл.почты',
            'first_name': 'Ваше имя',
            'last_name': 'Ваша фамилия',
        }
        widgets = {
            'first_name': TextInput(attrs={'required': True}),
            'last_name': TextInput(attrs={'required': True})
        }


class TaskForm(ModelForm):

    files = FileField(widget=ClearableFileInput(attrs={'multiple': True}), required=False, label='ФАЙЛЫ')

    class Meta:
        model = Task
        fields = ('title', 'desc', 'category', 'location', 'price', 'period_of_execution', 'author')
        labels = {
            'title': 'МНЕ НУЖНО',
            'desc': 'ПОДРОБНОСТИ ЗАДАНИЯ',
            'category': 'КАТЕГОРИЯ',
            'files': 'ФАЙЛЫ',
            'location': 'ЛОКАЦИЯ',
            'price': 'БЮДЖЕТ',
            'period_of_execution': 'СРОК ИСПОЛНЕНИЯ'
        }
        widgets = {
            'author': HiddenInput(),
            'period_of_execution': DateInput(attrs={'type': 'date'})
        }