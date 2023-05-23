from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('pomodoro',views.pomodoro,name='pomodoro'),
    path('todolist',views.todolist,name='todolist'),
    path('toreadlist',views.toreadlist,name='toreadlist'),
    path('notes',views.notes,name='notes'),



]