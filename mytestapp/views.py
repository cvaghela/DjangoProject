# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render


from django.http import HttpResponse

def hello(request):
   text = """<h1>Welcome to My Test App!</h1>"""
   return HttpResponse(text)