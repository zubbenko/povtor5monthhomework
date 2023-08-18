from movie_app import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/numberone', views.testir_api_view),
    path('api/v1/directors', views.director_list_api_view),
    path('api/v1/movies', views.movie_list_api_view),
    path('api/v1/reviews', views.review_list_api_view),
]
