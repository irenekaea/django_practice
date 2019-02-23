from django.urls import path
from . import views # Import all views from this folder

urlpatterns = [
    path('', views.index, name='index'),# Root path = ''
    path('about', views.about, name='about'), #views.method (in the views.py)
]