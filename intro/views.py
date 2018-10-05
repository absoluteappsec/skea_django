from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import TodoUserCreationForm, TodoForm
from .models import Todo

# Create your views here.
def index(request):
	return HttpResponse("Welcome to Seth & Ken's Excellent Adventures (in Code Review). Party on, dudes!")

@login_required
def todo(request, todo_id):
	if request.method == 'GET': 
		try:
			todo = Todo.objects.get(pk=todo_id,owner=request.user)
			form = TodoForm(initial={'todo_text':todo.todo_text,
									 'todo_date':todo.todo_date,
									 'completed':todo.completed})
		except Todo.DoesNotExist:
			raise Http404("Todo does not exist")
		return render(request, "todo_update.html", {'todo': todo, 'form': form} )
	elif request.method == 'POST':
		form = TodoForm(request.POST)
		if form.is_valid():
			try:
				todo = Todo.objects.get(pk=todo_id,owner=request.user)
			except Todo.DoesNotExist:
				raise Http404("Todo does not exist")
			
			todo.todo_text = form.cleaned_data['todo_text']
			todo.todo_date = form.cleaned_data['todo_date']
			todo.completed = form.cleaned_data['completed']
			todo.save()

	return HttpResponseRedirect('/intro/todos/')

@login_required
def create_todo(request):
	if request.method == 'POST':
		form = TodoForm(request.POST)
		if form.is_valid():
			t = Todo( todo_text=form.cleaned_data['todo_text'],
					  todo_date = form.cleaned_data['todo_date'],
					  completed = form.cleaned_data['completed'])
			t.owner = request.user
			t.save()
			return HttpResponseRedirect('/intro/todos/')
		
	else:
		form = TodoForm()
		
	return render(request,'todo.html',{'form': form})

@login_required
def todos(request):
	todos = Todo.objects.filter(completed=False,owner=request.user)
	return render(request,'todos.html',{'todos': todos})

@login_required
def todos_completed(request):
	todos = Todo.objects.filter(completed=True,owner=request.user)
	return render(request,'todos.html',{'todos': todos})

class SignUp(generic.CreateView):
	form_class = TodoUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'
	
