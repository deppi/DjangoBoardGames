from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response
from tictactoe.models import Game

import datetime

# ------- NOTES ---------- #
# Views do not create any presentation logic

class HelloWorldView(TemplateView):
	template_name = "helloworld.html"
	
	def get_context_data(self, **kwargs):
		return {"date": Game.objects.get(pk=1)}

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        return {"date": datetime.datetime.now()}

class LoggedOutView(TemplateView):
    template_name = "logged_out.html"
