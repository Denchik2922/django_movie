from .models import * 
from django.views.generic import ListView, DetailView, View, CreateView
from django.views.generic.detail import SingleObjectMixin

class ContextMixin(object):
	def get_context_data(self, **kwargs):
		context = super(ContextMixin, self).get_context_data(**kwargs)
		ganres = Ganre.objects.all()
		years = Year.objects.all()
		search = self.request.GET.get('search')
		search_year = self.request.GET.get('year')
		query = ""
		if search:
			query += f'search={search}&'
		if search_year:
			query += f'year={search_year}&'	

		context['years'] = years
		context['search'] = query
		context['ganres'] = ganres
		return context

