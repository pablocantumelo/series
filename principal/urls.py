# Imports
from django.urls import path
from . import views

# Configurando as URLs

urlpatterns = [
    path('',views.index,name='index')
]

