from django.db import models
from django.urls import reverse

# Create your models here.

class newTodo(models.Model):
	Todo = models.CharField(max_length = 256)

	def __str__(self):
		return self.Todo

	def get_absolute_url(self):
		return reverse('todos:todoList',kwargs={'pk':self.pk})
