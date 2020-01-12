from django.urls import path, include
from .views import *

urlpatterns = [
	path('', MovieListView.as_view(), name = 'movie_list_url'),
	path('<str:slug>/', MovieDetailView.as_view(), name = 'movie_detail_url'),
	path('<str:slug>/addreview/', ReviewCreateView.as_view(),
		 name = 'add_reveiw_url'),
	path('<str:slug>/edit_review/', ReviewEditView.as_view(),
		 name = 'edit_reveiw_url'),
	path('<str:slug>/delete_review/', ReviewDeleteView.as_view(),
		 name = 'delete_reveiw_url'),



] 