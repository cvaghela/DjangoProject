# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render

def hello(request):
   return render(request, "hello.html", {})