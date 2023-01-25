from django.http import HttpResponse
from django.shortcuts import render
from .forms import EquipmentsForm, FormList
from .models import *
from django import forms

def index(request):
    return render(request, 'index.html')

def form_in(request):
    if request.method == 'POST':
        # w1 = request.form.get('n1')

        t = request.POST.get('Typ')
        types = TypesEquipments.objects.create(TypesEq=t)
        types.save()
        return HttpResponse(f'<h2>{t} успешно добавлен в справочник!</h2><a href="/input_data/form_in"> '
                            f'Добавить еще!</a><br><br><a href="/">Вернуться на главную</a>')
    else:
        useform = EquipmentsForm()
        return render(request, 'form_index.html', {'form': useform})

def test(request):
    a = 'drgdsghfdghbfgdbd'
    return HttpResponse(a)

def st2(request):
    return render(request, 'formsinput.html')

def form_tabs(request):
    form = EquipmentsForm()
    if request.method == 'POST':
        if request.POST.get('forms') == 'formOne':
            print('Forma One')
            print(request.POST.get('forms'))
        elif request.POST.get('forms') == 'formTwo':
            print('Forma Two')

    return render(request, 'form_tabs.html', {'form': form})

def form_list(request):

    ch = ('one', 'two', 'fre', 'fo', 'six', 'seven', 'apple', 'pe', 'green', 'blue', 'mas', 'mon', 'con', 'mea', 'mya', 'moa')
    form = FormList()
    lst2 = request.method
    print('lst2', lst2)
    if request.method == 'POST':

        lst = request.POST.get('select')
        print(lst)

    return render(request, 'form_list.html', {'form': form, 'ch': ch})





# Create your views here.
