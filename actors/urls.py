from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ActorListView.as_view(), name = 'actor_list_url'),

]