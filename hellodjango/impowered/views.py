from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
import datetime

from models import *
from django.contrib.auth.models import User

@login_required
def home(request):
    user = request.user
    return render(request, "index.html")
    
def skill_tree(request):
	user = User.objects.all()[0]
	
	st_json = node_json(user.profile.skills.get(pk=3))
	st_json = st_json[:-1] + ' '
	
	return render(request, "skill_tree.html", 
		{'user':user, 
		 'st_json': st_json},)
	
def skill_tree2(request):
	user = User.objects.all()[0]
	return render(request, "skill_tree2.html", {'user':user},)
	
def node_json(skill):
	ret_json = "{"
	ret_json += "id: \"node" + str(skill.id) + "\","
	ret_json += "name: \"" + skill.name + "\","
	ret_json += "data: {progress: "+ str(100*skill.get_percentage_complete()) +"},"
	ret_json += "children: ["
	for child in Skill.objects.filter(parent=skill.id):
		ret_json += node_json(child)
	ret_json += "],"
	ret_json += "},"
	return ret_json