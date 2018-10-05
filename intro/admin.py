from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import TodoUserCreationForm, TodoUserChangeForm
from .models import TodoUser

class TodoUserAdmin(UserAdmin):
    add_form = TodoUserCreationForm
    form = TodoUserChangeForm
    model = TodoUser
    list_display = ['email', 'username',]

admin.site.register(TodoUser, TodoUserAdmin)