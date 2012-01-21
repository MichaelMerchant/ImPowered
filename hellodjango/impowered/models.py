from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
	uid = models.OneToOneField(User, related_name = "profile")	
	
	def __unicode__(self):
		return self.uid.username
	
class Skill(models.Model):
	user = models.ForeignKey(Profile, related_name = "skills")
	name = models.CharField(max_length = 200)
	parent = models.ForeignKey( 'self' , related_name = "parent_skill", null = True, blank = True)
	points_possible = models.IntegerField(default = 10000)

	def get_progress_points(self):
		sum = 0
		for child in Skill.objects.filter(parent=self.id):
			sum += child.get_progress_points()
		for goal in Goal.objects.filter(skill=self.id):
			sum += goal.get_percentage_complete() * goal.point_value
		if sum > self.points_possible:
			return self.points_possible
		return sum

	def get_percentage_complete(self):
		return self.get_progress_points()/self.points_possible
		
	def __unicode__(self):
		return self.name

class Goal(models.Model):
	skill = models.ForeignKey(Skill, related_name = "goals")
	name = models.CharField(max_length = 200)
	hours_estimated = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	point_value = models.IntegerField(default = 10)
	
	def get_hours_completed(self):
		sum = 0
		for point in self.data.all():
			sum += point.value
		return sum

	def get_hours_left(self):
		value = self.get_hours_completed()-self.hours_estimated
		if(value<0):
			return 0
		return value
	
	def get_percentage_complete(self):
		return self.get_hours_completed()/self.hours_estimated
	
	def __unicode__(self):
		return self.name

class DataPoint(models.Model):
	goal = models.ForeignKey(Goal, related_name = "data")
	value = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	
	def __unicode__(self):
		return str(self.goal) + ": " + str(self.value)