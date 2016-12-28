# AccessMasterGridView/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.db import connections
import MySQLdb

from .models import AccessMaster

# Create your views here.

#class HomePageView(TemplateView):
#	def get(self, request, **kwargs):
#		db = MySQLdb.connect("localhost","root","root","stores" )
#		cursor = db.cursor()
#		cursor.execute("SELECT access_name from access_master limit 5")
#		posts = cursor.fetchall()
#		db.close()
#		return render(request, 'index.html', {'posts':posts})

class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		posts= AccessMaster.objects.values_list('access_id', 'access_name', 'access_email').order_by('access_name')
		return render(request, 'index.html', {'posts':posts})

class AboutPageView(TemplateView):
	template_name = "about.html"