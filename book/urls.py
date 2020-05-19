from django.urls import path
from . import views

urlpatterns = [

path("home",views.home,name="home"),
path("slambook",views.slambook,name="slambook"),
path('thank',views.thank,name='thank'),


]