from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .forms import *

def index(request):
    return render(request, 'index.html')


def laptop_views(request):
    items = Laptop.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(items, 10)
    try:
        item = paginator.page(page)
    except PageNotAnInteger:
        item = paginator.page(1)
    except EmptyPage:
        item = paginator.page(paginator.num_pages)
    context = {'items': item,
               'header': 'Laptops'}
    return render(request, 'index.html', context)


def desktop_views(request):
    items = Desktop.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(items, 10)
    try:
        item = paginator.page(page)
    except PageNotAnInteger:
        item = paginator.page(1)
    except EmptyPage:
        item = paginator.page(paginator.num_pages)
    context = {'items': item,
               'header': 'Desktops'}
    return render(request, 'index.html', context)


def mobile_views(request):
    items = Mobile.objects.all()
    context = {'items': items,
               'header': 'Mobiles'}
    return render(request, 'index.html', context)


def add_device(request, cls):

    if request.method == 'POST':
        form = cls(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls
        return render(request, 'add_device.html', {'form': form})


def add_laptop(request):
    return add_device(request, LaptopForm)


def add_desktop(request):
    return add_device(request, DesktopForm)


def add_mobile(request):
    return add_device(request, MobileForm)


def edit_divice(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)
        print()
        return render(request, 'edite_divice.html', {'form': form})


def edit_laptop(request, pk):
    return edit_divice(request, pk, Laptop, LaptopForm)


def edit_desktop(request, pk):
    return edit_divice(request, pk, Desktop, DesktopForm)


def edit_mobile(request, pk):
    return edit_divice(request, pk, Mobile, MobileForm)


def delete_laptop(request, pk):
     Laptop.objects.filter(id=pk).delete()
     items = Laptop.objects.all()
     context = {'items':items}
     return redirect('laptop_views')


def delete_desktop(request, pk):
    Desktop.objects.filter(id=pk).delete()
    items = Desktop.objects.all()
    context = {'items': items}
    return redirect('desktop_views')


def delete_mobile(request, pk):
    Mobile.objects.filter(id=pk).delete()
    items = Mobile.objects.all()
    context = {'items': items}
    return redirect('mobile_views')