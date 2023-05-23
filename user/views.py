from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django import forms



def signin(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:

            login(request, user)
            redirect('home')
        else:
            messages.success(request,"there was a mistake, try again")


    else:
        return render(request, 'user/login.html', {})





    return render(request, 'user/login.html')



def signout(request):

    logout(request)
    messages.success(request, "you did sign out successfully")
    return redirect('home')




def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,("account was made successfully"))
            return redirect('home')
        else:
            form = UserCreationForm()
        return render(request, 'user/signup.html',{'form':form,})





    return render(request,'user/signup.html')
