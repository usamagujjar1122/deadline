from . import views
from django.urls import path

urlpatterns = [
    path('signout', views.signout, name='signout'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),



]