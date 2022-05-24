from django.shortcuts import render
from .models import Crypto

def home(request):
    projects = Crypto.objects.all()
    return render(request, 'about_crypto/home.html', {'projects':projects})
