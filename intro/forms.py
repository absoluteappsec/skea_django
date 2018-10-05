# intro/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
import datetime

from .models import TodoUser

class TodoUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = TodoUser
        fields = ('username', 'first_name', 'last_name', 'email')

class TodoUserChangeForm(UserChangeForm):

    class Meta:
        model = TodoUser
        fields = ('username', 'first_name', 'last_name', 'email')


class TodoForm(forms.Form):
	todo_text = forms.CharField(label="Todo", max_length=2048)
	todo_date = forms.DateField(label="Date", initial=datetime.date.today)
	completed = forms.BooleanField(label="Completed",initial=False,required=False)