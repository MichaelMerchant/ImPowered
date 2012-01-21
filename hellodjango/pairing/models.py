from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import models

class StudentProfile(models.Model):
	uid = models.OneToOneField(User, related_name="student_profile")
	email = models.CharField(max_length = 50, blank=True, null=True)
	phone = models.CharField(max_length = 20, blank=True, null=True)
	facebook_url = models.CharField(max_length = 200, blank=True, null=True)
	
	def __unicode__(self):
		return self.uid.get_full_name()

	def is_available(self, project):
		for pair in project.pairings.all():
			if pair.state == "P" and (pair.student1 is self or pair.student2 is self):
				return False
		return True

	def get_relationship(self, other_student, project):
		for pair in project.pairings.all():
			if pair.student1 == self and pair.student2 == other_student:
				if pair.state == "P" or pair.state == "I":
					return "Waiting to hear back"
				else:
					return "Paired Together"
			elif pair.student1 == other_student and pair.student2 == self:
				if pair.state == "P" or pair.state=="I":
					return "Invited to Partner"
				else:
					return "Paired Together"
		return "None"


class Project(models.Model):
	students = models.ManyToManyField(StudentProfile, related_name="projects", null=True)
	name = models.CharField(max_length = 100)
	
	def __unicode__(self):
		return self.name

PAIRING_STATES=(("C","Completed"),("P","Proposed"),("I","Ignored"))

class Pairing(models.Model):
	project = models.ForeignKey(Project, related_name="pairings")
	#student 1 is the proposer
	student1 = models.ForeignKey(StudentProfile, related_name="initiated_pairings")
	#student 2 is the accepter
	student2 = models.ForeignKey(StudentProfile, related_name="invited_pairings")
	#student 3 is an accepter and may not be possible. To be implemented
	#student3 = models.ManyToManyField(StudentProfile, related_name="pairings", null=True, blank=True)
	state = models.CharField(max_length = 20, choices=PAIRING_STATES, default="P")
	
	def __unicode__(self):
		return str(self.student1) + " & " + str(self.student2)