from django.urls import path
from . import views

app_name = 'bitcoin'

urlpatterns = [
    path('', views.index, name="index"),
]