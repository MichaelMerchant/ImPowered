from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from models import *
from simplejson import dumps
from utils import jsonify

def home(request):
	return render(request, "pairing/index.html", {'projects':Project.objects.all()})

@login_required
def student_listing(request, project_id):
	project = Project.objects.get(pk=project_id)
	return render(request, "pairing/student_listing.html", {'project':project})
	
def student_row(request, other_sid, pid):
	return jsonify({
					'row_html':student_row_html(request, other_sid, pid),
					'student_id':other_sid,
					'project_id':pid,
					})

@login_required
def student_row_html(request, other_sid, pid):
	other_student = StudentProfile.objects.get(pk=other_sid)
	project = Project.objects.get(pk=pid)
	if not other_student.is_available(project):
		actions = "Paired Up"
	elif request.user.is_authenticated():
		current_student = request.user.student_profile
		if current_student==other_student:
			actions = ""
		else:
			actions = available_actions(current_student, other_student, project)
	else:
		actions = ""
	return render(request, "pairing/student_listing_row.html", 
						{"student": other_student,
						"available_action":actions}).content

@login_required
def accept(request, sid, pid):
	pass

@login_required
def cancel(request, sid, pid):
	pass

@login_required
def invite(request, sid, pid):
	user = request.user.student_profile
	other_student = StudentProfile.objects.get(pk=sid)
	project = Project.objects.get(pk=pid)
	if(user.get_relationship(other_student, project) == "None"):
		new_pairing = Pairing(student1=user, student2=other_student, project=project)
		new_pairing.save()
		return jsonify({'status':'success',
					'user_id':user.pk,
					'student_id':other_student.pk,
					'project_id':project.pk,
					'row_html':student_row_html(request, sid, pid),
				})
	else:
		return jsonify({'status':'RelationExists',
					'user_id':user.pk,
					'student_id':other_student.pk,
					'project_id':project.pk,
					'row_html':student_row_html(request, sid, pid),})

def available_actions(user, considered_student, project):
	if user.is_available(project):
		current_situation = user.get_relationship(considered_student, project)
		if(current_situation=="Waiting to hear back"):
			return "Waiting"
		elif current_situation == "Paired Together":
			return "My partner"
		elif current_situation == "Invited to Partner":
			return "Accept?"
		else:#No relationship
			return "Propose"
	return ""