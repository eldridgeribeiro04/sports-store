from typing import Any
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Brand
# from django.views.generic import TemplateView
# Create your views here.

def home(request):
    # template = loader.get_template("home.html")
    brands = Brand.objects.all()
    return render(request, "product/home.html", {
        "brands":brands})