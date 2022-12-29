from django.shortcuts import render
from .models import *

def index(request):
    cartoons=Cartoon.objects.all()
    context={
        'cartoons': cartoons
    }
    return render(request, 'index.html', context)