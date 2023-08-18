from django.contrib import admin
from movie_app.models import Director
from movie_app.models import Review
from movie_app.models import Movie

admin.site.register(Director)
admin.site.register(Review)
admin.site.register(Movie)