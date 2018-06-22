from django.db import models

# Create your models here.

class newTodo(models.Model):
	Todo = models.CharField(max_length = 256)

	def __str__(self):
		return self.Todo
