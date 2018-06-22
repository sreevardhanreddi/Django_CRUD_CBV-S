from django.conf.urls import url
from . import views

app_name = 'todos'

urlpatterns = [
	url(r'^index/$',views.IndexView.as_view(),name='index'),
	url(r'^todoList/$',views.TodoListView.as_view(),name='todoList'),
	url(r'^todoListDelete/(?P<pk>\d+)$',views.TodoDeleteView.as_view(),name='todoListDelete'),
	# (?# url(r'^index2/$',views.IndexView2.as_view(),name='index2'),)

]