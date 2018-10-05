from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class TodoUser(AbstractUser):
	
	def __str__(self):
		return self.email

class Todo(models.Model):
	todo_text = models.TextField()
	todo_date = models.DateTimeField('date')
	completed = models.BooleanField(default=False)
	owner = models.ForeignKey(TodoUser, on_delete=models.CASCADE)
		