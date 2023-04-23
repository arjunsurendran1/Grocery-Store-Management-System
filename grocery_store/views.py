from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import *

from .forms import *

#function for home 
def index(request):
    return render(request, 'gstore/index.html')

#for display
def display_rice(request):
    items = Rice.objects.all()
    context = {
        'items': items,
        'header': 'Rice',
    }
    return render(request, 'gstore/index.html', context)


def display_bakery(request):
    items = Bakery.objects.all()
    context = {
        'items': items,
        'header': 'Bakery',
    }
    return render(request, 'gstore/index.html', context)


def display_dairy(request):
    items = Dairy_products.objects.all()
    context = {
        'items': items,
        'header': 'Dairy Products',
    }
    return render(request, 'gstore/index.html', context)


def display_drinks(request):
    items = Drinks.objects.all()
    context = {
        'items': items,
        'header': 'Drinks',
    }
    return render(request, 'gstore/index.html', context)

def display_spices(request):
    items = Spices.objects.all()
    context = {
        'items': items,
        'header': 'Spices',
    }
    return render(request, 'gstore/index.html', context)


#for add items
def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'gstore/add_new.html', {'form' : form})


def add_rice(request):
    return add_item(request, RiceForm)


def add_bakery(request):
    return add_item(request, BakeryForm)


def add_dairy(request):
    return add_item(request, DairyForm)

def add_drinks(request):
    return add_item(request, DrinksForm)

def add_spices(request):
    return add_item(request, SpicesForm)


#edit items
def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'gstore/edit_item.html', {'form': form})



def edit_rice(request, pk):
    return edit_item(request, pk, Rice, RiceForm)


def edit_bakery(request, pk):
    return edit_item(request, pk, Bakery, BakeryForm)


def edit_dairy(request, pk):
    return edit_item(request, pk, Dairy_products,DairyForm)


def edit_drinks(request, pk):
    return edit_item(request, pk,Drinks,DrinksForm)


def edit_spices(request, pk):
    return edit_item(request, pk, Spices,SpicesForm)

#for delete items
def delete_rice(request, pk):

    template = 'gstore/index.html'
    Rice.objects.filter(id=pk).delete()

    items = Rice.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_bakery(request, pk):

    template = 'gstore/index.html'
    Bakery.objects.filter(id=pk).delete()

    items = Bakery.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_dairy(request, pk):

    template = 'gstore/index.html'
    Dairy_products.objects.filter(id=pk).delete()

    items = Dairy_products.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_drinks(request, pk):

    template = 'gstore/index.html'
    Drinks.objects.filter(id=pk).delete()

    items = Drinks.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_spices(request, pk):

    template = 'gstore/index.html'
    Spices.objects.filter(id=pk).delete()

    items = Spices.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)

