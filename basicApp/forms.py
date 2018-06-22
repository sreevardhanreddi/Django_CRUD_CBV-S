from django import forms
from django.core import validators
from basicApp.models import newTodo


class todoForm(forms.ModelForm):
	# todo =forms.CharField()
	class Meta():
		model = newTodo
		fields = '__all__'
