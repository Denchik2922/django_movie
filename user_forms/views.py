from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import AuthUserForm, RegisterUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
class UserLoginView(LoginView):
	template_name = 'movies/movie_list.html'
	form_class = AuthUserForm
	success_url = reverse_lazy('movie_list_url')
	def get_success_url(self):
		return self.success_url	

class UserLogoutView(LogoutView):
	next_page = reverse_lazy('movie_list_url')	

class UserRegisterView(CreateView):
	template_name = 'movies/movie_list.html'
	model = User
	form_class = RegisterUserForm	
	success_url = reverse_lazy('movie_list_url')

	def form_valid(self, form):
		form_valid = super().form_valid(form)
		username = form.cleaned_data['username']	
		password = form.cleaned_data['password']
		auth_user = authenticate(username = username, password = password)
		login(self.request, auth_user)
		return form_valid
