from django.http import HttpResponse
from simplejson import dumps
from django.shortcuts import render

def jsonify(response):
    return HttpResponse(dumps(response), mimetype="application/json")
