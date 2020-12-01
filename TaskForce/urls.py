from django.urls import path
from .views import index, UserLogin, UserRegister, CreateTask, ShowTasks, ShowTask
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('tasks/<int:pk>/', ShowTask.as_view(), name='detail'),
    path('tasks/', ShowTasks.as_view(), name='index'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('login/', UserLogin.as_view(), name='login'),
    path('reg/', UserRegister.as_view(), name='reg'),
    path('create/', CreateTask.as_view(), name='create_task'),
]