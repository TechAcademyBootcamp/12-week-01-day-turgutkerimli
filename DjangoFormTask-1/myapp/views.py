from django.shortcuts import render
from .forms import AddressForm

# Create your views here.

def form_func(request):
    context = {
        'form': AddressForm()
    }
    return render(request, 'form.html', context)