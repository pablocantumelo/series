from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from . import forms
from . import models

# Create your views here.
def cadastro(request):
    print( " e n t r o u ....")
    form = forms.SerieForm()
    if request.method == 'POST':
        form = forms.SerieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print(" ERRO ")
    serie_items=models.Serie.objects.order_by('nome')
    data_dict = {'serie_record': serie_items,'form': form}
    return render(request,'serie/serie.html',data_dict)

