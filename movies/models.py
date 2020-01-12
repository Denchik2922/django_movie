from django.db import models
from django.shortcuts import reverse
from datetime import date
from django.contrib.auth.models import User


class Actor(models.Model):
	'''Model for movie actors'''
	name = models.CharField("Имя", max_length = 100)
	age = models.SmallIntegerField("Возраст", default = 0)
	description = models.TextField("Описание")
	image = models.ImageField("Изображение", upload_to = "actors/")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Актеры и режиссеры "
		verbose_name_plural = "Актеры и режиссеры"	

class Ganre(models.Model):
	'''Model for movie ganres'''
	name = models.CharField("Жанр", max_length = 100) 	
			

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Жанр"
		verbose_name_plural = "Жанры"
class Year(models.Model):
	'''Model for movie years'''		
	year =  models.SmallIntegerField("Год", default = 2000)

	def __str__(self):
		return str(self.year)


	class Meta:
		verbose_name = "Год"
		verbose_name_plural = "Год"

class Movie(models.Model):
	'''Model for movie'''
	title = models.CharField("Фильм", max_length = 100) 
	description = models.TextField("Описание")
	poster = models.ImageField("Изображение", upload_to = "movies/")
	year = models.ForeignKey(Year,verbose_name='Дата выхода', default = 2000,
							 on_delete = models.SET_NULL, null = True)
	country = models.CharField("Страна", max_length = 100)
	directors = models.ManyToManyField(Actor, verbose_name = 'Режиссер',
									   related_name = 'movie_derectors')
	actors = models.ManyToManyField(Actor, verbose_name = 'Актеры',
									related_name = 'movie_actors')
	ganres = models.ManyToManyField(Ganre, verbose_name = 'Жанры')
	world_premiere = models.DateField("Примьера в мире", default = date.today)
	budget = models.PositiveIntegerField(
		"Бюджет", default = 0, help_text = "Указывать сумму в долларах"
	)
	fees_in_usa = models.PositiveIntegerField(
		"Сборы в США", default = 0, help_text = "Указывать сумму в долларах"
	)
	fees_in_world = models.PositiveIntegerField(
		"Сборы в Мире", default = 0, help_text = "Указывать сумму в долларах"
	)
	url = models.SlugField(max_length = 150, unique = True)
	draft = models.BooleanField("Черновик", default = False)		

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('movie_detail_url', kwargs = {'slug':self.url})	

	def get_review(self):
		return self.review_set.filter(parent__isnull=True)

	class Meta:
		verbose_name = "Фильм"
		verbose_name_plural = "Фильмы"	
		ordering = ['-year']

class MovieShots(models.Model):
	'''Model for movie shots'''
	title = models.CharField("Заголовок", max_length = 100)  		
	image = models.ImageField("Изображение", upload_to = "movie_shots/")
	movie =  models.ForeignKey(Movie, verbose_name = "Фильм",
							   on_delete = models.CASCADE)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Кадр из фильма"
		verbose_name_plural = "Кадры из фильма"	

class RatingStars(models.Model):
	'''Model for rating stars'''
	velue = models.PositiveSmallIntegerField("Значение", default = 0)

	def __str__(self):
		return self.velue

	class Meta:
		verbose_name = "Звезда рейтингa"
		verbose_name_plural = "Звезды рейтингa"

class RatingMovie(models.Model):
	'''Model for movie rating'''
	ip = models.CharField("IP адрес", max_length = 15)
	movie =  models.ForeignKey(Movie, verbose_name = "Фильм",
							   on_delete = models.CASCADE)
	star = models.ForeignKey(RatingStars ,verbose_name = "Звезда",
							 on_delete = models.CASCADE)

	def __str__(self):
		return f"{self.star} - {self.movie}"

	class Meta:
		verbose_name = "Рейтинг"
		verbose_name_plural = "Рейтинги"	

class Review(models.Model):
	'''Model for movie reviews'''
	
	name = models.ForeignKey(User, verbose_name = "Имя", on_delete = models.CASCADE)
	text = models.TextField("Сообщение", max_length = 5000)
	movie = models.ForeignKey(Movie, verbose_name = "Фильм",
							  on_delete = models.CASCADE)
	parent = models.ForeignKey('self', verbose_name='Родитель',
							   on_delete=models.CASCADE, blank=True, null=True )
	pub_date = models.DateTimeField('Дата комментария',
									auto_now_add=True)

							   		 		

	def __str__(self):
		return f"{self.name} - {self.movie}"

	class Meta:
		verbose_name = "Отзыв"
		verbose_name_plural = "Отзывы"
		ordering = ['-pub_date']