from django.urls import path

from . import views

app_name = "movies"

urlpatterns = [
   path("", views.home, name="home"),
   path("cookies", views.cookies, name="cookies"),
   path("create", views.create, name="create"),
#    path("movie_list", views.movie_list, name="movie_list"),
]