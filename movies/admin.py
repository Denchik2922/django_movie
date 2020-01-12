from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Review)
admin.site.register(RatingMovie)
admin.site.register(RatingStars)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Ganre)
admin.site.register(Actor)

admin.site.register(Year)