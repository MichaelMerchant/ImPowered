"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from impowered.models import *
from django.contrib.auth.models import User

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class FirstTest(TestCase):
	def setup(self):
		self.user = User(username="tester", password="pass")
		
	
	
	def test_goals_adding_data_point(self):
		