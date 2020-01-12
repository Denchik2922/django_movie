from django.shortcuts import render
from movies.models import Actor
from django.views.generic import ListView

class ActorListView(ListView):
	model = Actor
	queryset = Actor.objects.all()
	template_name = 'actors/actor_list.html'




