from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def home(request):
    return render(request, 'home.html')
