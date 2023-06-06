from django.shortcuts import render , HttpResponse , redirect

# Create your views here.
from app.models import arvoreDetalhe , controleEntrega


def primeiroRender(request):
    return render(request , 'home.html')