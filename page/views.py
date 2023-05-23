from django.shortcuts import render ,redirect
from django.contrib import admin
from . import views
from django.http import HttpResponse
from django.contrib.auth.models  import User
from django.contrib import messages



# Create your views here.
def home(request):
    return render(request,'page/home.html')
def pomodoro(request):
    return render(request,'page/pomodoro.html')
def todolist(request):
    return render(request,'page/todolist.html')
def toreadlist(request):
    return render(request,'page/toreadlist.html')
def notes(request):
    return render(request,'page/notes.html')












