from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html'), name='password'),
    path('<int:todo_id>/',views.todo, name='todo'),
    path('todo/',views.create_todo, name='create todo'),
    path('todos/',views.todos, name='todos'),
    path('todos/completed/',views.todos_completed, name='completed todos')
]
