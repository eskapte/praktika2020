from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, FormView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin, UpdateView

from .forms import RegisterUserForm, TaskForm, ApplicationForm
from .models import Task, Category, Document, Profile, Application


class ShowTasks(ListView):
    template_name = 'TaskForce/tasks.html'
    queryset = Task.objects.all()
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = Task.cities
        context['categories'] = Category.objects.all()
        context['active_categories'] = self.request.GET.getlist('category')
        return context

    def get(self, request, *args, **kwargs):
        # Сортировка по категориям
        if self.request.GET.getlist('category'):
            self.queryset = Task.objects.filter(Q(category__name__in=self.request.GET.getlist('category')))
        return super().get(request, args, kwargs)


def index(request):
    tasks = Task.objects.all()
    cities = Task.cities
    categories = Category.objects.all()
    return render(request, 'TaskForce/tasks.html', {'tasks': tasks, 'cities': cities, 'categories': categories})


class UserLogin(LoginView):
    template_name = 'TaskForce/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = Task.cities
        return context

    def get_redirect_url(self):
        self.next = super().get_redirect_url()
        if self.next:
            return self.next
        self.next = '/tasks'
        return self.next


class UserRegister(CreateView):
    template_name = 'TaskForce/registration.html'
    form_class = RegisterUserForm
    model = User
    success_url = reverse_lazy('login')

    def get_success_url(self):
        is_customer = self.request.POST.get('role') == "Заказчик"
        user = User.objects.get(username=self.request.POST.get('username'))
        Profile.objects.create(user=user, is_customer=is_customer)
        return super().get_success_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = Task.cities
        return context


class CreateTask(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')

    template_name = 'TaskForce/create_task.html'
    form_class = TaskForm
    success_url = '/tasks'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = self.request.FILES.getlist('files')
        print(files)
        if form.is_valid():
            id = form.save().pk
            print(id)
            task = Task.objects.get(pk=id)
            if files:
                for f in files:
                    fl = Document.objects.create(task=task, file=f)
                    fl.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_initial(self):
        self.initial = super().get_initial()
        self.initial['author'] = self.request.user.pk
        return self.initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = Task.cities
        return context


class ShowTask(DetailView, FormView):
    model = Task
    template_name = 'TaskForce/detail.html'
    form_class = ApplicationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = Task.cities
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


    def post(self, request, *args, **kwargs):
        if self.request.POST.get('accept-work'):
            author = User.objects.get(username=self.request.user.username)
            task = Task.objects.get(pk=self.get_object().id)
            ans_price = self.request.POST.get('price')
            ans_text = self.request.POST.get('text')
            if ans_text:
                Application.objects.create(task=task, author=author, text=ans_text, price=ans_price).save()
            else:
                Application.objects.create(task=task, author=author, price=ans_price).save()
        return reverse_lazy('index')

