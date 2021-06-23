from django.urls import path
from . import views

urlpatterns = [
    path('',views.cadastro,name = 'Cadastro'),
    path('delete/<ids>',views.delete,name = 'Deletar'),
    path('update/<ids>',views.update,name = 'Atualizar')
]