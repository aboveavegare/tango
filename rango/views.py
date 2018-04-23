# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context = {'aboutmessage': "Welcome! Here Rango tells about the project!", 'creator': "This project has been set up by TimL"}
    return render(request, 'rango/about.html', context=context)
