from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Menu
from django.contrib.auth.decorators import login_required
from .forms import OrderForm

# Create your views here.

@login_required
def items(request):
    items = Menu.objects.all()
    data = {
        'items':items,
    }
    return render(request,'menus/items.html',data)

@login_required
def orders(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.save()
            form.save_m2m()  # always required when save(commit=False) and we have many-to-many field.
            messages.success(request,'Thanks for ordering from us....')
        else:
            messages.error(request,'Some error occurred')
        return redirect('home')

    form = OrderForm()
    data = {
        'form':form,
    }

    return render(request,'menus/orders.html',data)

