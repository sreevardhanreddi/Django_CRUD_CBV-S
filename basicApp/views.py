from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,ListView,DeleteView,UpdateView,CreateView
from django.http import request
from django.urls import reverse_lazy,reverse
from basicApp.forms import todoForm
from basicApp.models import newTodo
# Create your views here.


class IndexView(View):
	
	def get(self,request):
		form = todoForm()
		return render(request,'basicApp/index.html',{'form':form})


	def post(self,request):
		form = todoForm()

		if(request.method == 'POST'):
			
			form = todoForm(request.POST)
			
			#the below code for server side validation
			if(form.is_valid()):
				print('recieved')
				# print(form)
				print('processing')
				print("recieved data is ==>", form.cleaned_data['Todo'])
				form.save()
				print('data saved')
				# print(form.todo)

				return redirect('todos:index')

		return render(request,'basicApp/index.html',{'form':form})
			


class TodoListView(ListView):
	template_name='basicApp/views.html'
	context_object_name = 'todos'
	model = newTodo



class TodoDeleteView(DeleteView):
	model = newTodo
	template_name='basicApp/confirm.html'
	# success_url = reverse_lazy('todoList')

	def get_success_url(self):
		return reverse('todos:todoList')


class TodoUpdateView(UpdateView):
	template_name = 'basicApp/index.html'
	model = newTodo
	fields = ('Todo',)

	# def get_success_url(self):
	# 	return reverse('todos:todoList')