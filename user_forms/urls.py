from django.urls import path
from .views import UserLoginView, UserLogoutView, UserRegisterView


urlpatterns = [
	path('register/', UserRegisterView.as_view(), name='register_url'),
    path('login/', UserLoginView.as_view(), name='login_url'),
    path('logout/', UserLogoutView.as_view(), name='logout_url'),
    

    
  

    
]