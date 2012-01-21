from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
import datetime
import re
from data import data, api_key

from models import *
from django.contrib.auth.models import User

def home(request):
    return render(request, "eweekmap/index.html", {'data':cleanData(data)})

def cleanData(data):
    new_data =[]
    for datum in data:
        new_data.append(cleanDatum(datum))
    return new_data

def cleanDatum(datum):
    html_pattern = r'[<][/]?[\w\s\"\\\=]*[/]?[>]'
    for key, value in datum.items():
        datum[key] = re.sub(html_pattern, ' ',  value)
    return datum

def test(request):
    return render(request, "eweekmap/example.html", {'api_key':api_key})