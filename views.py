from django.shortcuts import render    # To request web pages.
from django.contrib import messages    # To show messages on screen.
from .forms import Sell, Buy

# Create your views here.

def home(request):
    return render(request, 'Home/home.html')

def about(request):
    return render(request, 'Home/about.html')

def sell(request):
    if request.method == 'POST':
        s_form = Sell(request.POST, instance=request.user)    # form for selling energy.
        s_form.save()
        messages.success(request, f'Transaction Successful!')
    else:
        s_form = Sell()
    return render(request, 'Home/sell.html', {'form': s_form})

def buy(request):
    if request.method == 'POST':
        b_form = Buy(request.POST, instance=request.user)    # form for buying energy.
        b_form.save()
        messages.success(request, f'Transaction Successful!')
    else:
        b_form = Buy()
    return render(request, 'Home/buy.html', {'form': b_form})

def table(request):
    return render(request, 'Home/tables.html')

def goals(request):
    return render(request, 'Home/goals.html')

def partners(request):
    return render(request, 'Home/partners.html')

