from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from utils import jsonify
from django.contrib.auth import logout, authenticate, login
from django.core.urlresolvers import reverse

def myLogin(request):
    next_url = request.GET.get('next', '')
    if request.user.is_authenticated():
        if next_url=='':
            return HttpResponseRedirect(reverse('home'))
        return HttpResponseRedirect(next_url)
    if request.method == "GET":
        return render(request, "accounts/login.html",{'next':next_url})
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if next_url=='':
                return HttpResponseRedirect(reverse('home'))
            return HttpResponseRedirect(next_url)
        else:
            return render(request, "accounts/login.html",{'fail':True,'next':next_url})

def myLogout(request):
    logout(request)
    referer = request.META.get('HTTP_REFERER','')
    if referer == '':
        return HttpResponseRedirect(reverse('home'))
    return HttpResponseRedirect(referer)
