from django.urls import path
from . import views

urlpatterns = [
    path('naasu/',views.index,name='index')
]