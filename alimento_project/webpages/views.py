from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import QuickOrderForm
from .models import QuickOrder

# Create your views here.


def home(request):
    
    if request.method == 'POST':
        form = QuickOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
        messages.success(request,'Thank you for ordering from us, your order will be delivered soon....')
        return redirect('home')

    else:
        form = QuickOrderForm()
        data = {
            'form' : form,
        }

    return render(request,'webpages/home.html',data)