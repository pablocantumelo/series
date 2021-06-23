from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from . import forms
from . import models

# Create your views here.
def cadastro(request):
    form = forms.GeneroForm()
    if request.method == 'POST':
        form = forms.GeneroForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print(" ERRO ")
    genero_lista=models.Genero.objects.order_by('descricao')
    data_dict = {'form': form,'gereros_items': genero_lista}
    return render(request,'genero/genero.html',data_dict)

def delete(request,ids):
    try:
        models.Genero.objects.filter(id=ids).delete()
        form = forms.GeneroForm()
        genero_lista = models.Genero.objects.order_by('descricao')
        data_dict = {'form': form, 'gereros_items': genero_lista}
        return render(request, 'genero/genero.html', data_dict)
    except:
        return HttpResponseNotAllowed()


def update(request,ids):
    item = models.Genero.objects.get(id=ids);
    if request.method == "GET":
        form = forms.GeneroForm(initial={'descricao':item.descricao})
        print(form)
        data_dict = {'form': form}
        return render(request,'genero/genero_upd.html',data_dict)
    else:
        form = forms.GeneroForm(request.POST)
        item.descricao = form.data['descricao']
        item.save()
        genero_lista = models.Genero.objects.order_by('descricao')
        data_dict = {'form': form, 'gereros_items': genero_lista}
        return render(request, 'genero/genero.html', data_dict)
