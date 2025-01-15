from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='index'),
	path('leader_board/', views.leader_board, name='leader_board'),
	path('python_topic_1/', views.python_topic_1, name='python_topic_1') # TODO переделать
]
