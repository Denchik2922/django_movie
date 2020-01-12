from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View, CreateView
from .forms import ReviewForm
from django.db.models import Q
from .models import * 
from .utils import ContextMixin
# Create your views here.


class MovieListView(ContextMixin,ListView):
	model = Movie
	paginate_by = '12'

	
	
	def get_queryset(self):
		
		queryset = self.model.objects.filter(draft=False)
		if self.request.GET.get('search') and self.request.GET.get('year'):
			search = self.request.GET.get('search')
			year = self.request.GET.get('year')
			queryset = self.model.objects.filter(Q(draft=False),
												 Q(year__year__contains=year),	
												 Q(title__icontains=search)|
												 Q(description__icontains=search)|
												 Q(ganres__name__contains=search))
		elif self.request.GET.get('year'):
			year = self.request.GET.get('year')
			queryset = self.model.objects.filter(Q(draft=False),
												 Q(year__year__contains=year))
		elif self.request.GET.get('search'):
			search = self.request.GET.get('search')
			queryset = self.model.objects.filter(Q(draft=False),
											     Q(title__icontains=search)|
												 Q(description__icontains=search)|
												 Q(ganres__name__contains=search))	
			
		
		return queryset



	

class MovieDetailView(ContextMixin,DetailView):
	model = Movie
	slug_field = 'url'



class ReviewCreateView(View):
	def post(self, request, slug):
		if request.user.is_authenticated:
			form = ReviewForm(request.POST)
			movie = Movie.objects.get(url = slug)
			user = request.user
			if form.is_valid():
				form = form.save(commit=False)
				if request.POST.get("parent", None):
					form.parent_id = int(request.POST.get("parent"))
				form.name = user
				form.movie = movie
				form.save() 
			return redirect(movie.get_absolute_url())
		return redirect('movie_list_url')	 

class ReviewEditView(View):
	def post(self, request, slug):
		
		movie = Movie.objects.get(url = slug)
		id_rev = int(request.POST.get("id"))
		review = Review.objects.get(id=id_rev)
		
		if str(request.user.username).strip() == str(review.name).strip():

			form = ReviewForm(request.POST, instance = review)
			if form.is_valid():
				form.save()
				return redirect(movie.get_absolute_url()) 
		return redirect('movie_list_url')			

		
			

class ReviewDeleteView(View):
	def post(self, request, slug):

		movie = Movie.objects.get(url = slug)
		id_rev = int(request.POST.get("id"))
		
		review = Review.objects.get(id=id_rev)
		if str(request.user.username).strip() == str(review.name).strip() or request.user.is_staff:
			review.delete()
			return redirect(movie.get_absolute_url())
		return redirect('movie_list_url')		 		



	


	


		
	


