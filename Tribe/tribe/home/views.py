from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
