from django.urls import path

from movies.views import index, new_movies, move_detail


urlpatterns = [
    path('', index, name='main'),
    path('new_movies', new_movies, name='new_movies'),
    path('move_detail/<int:movie_id>', move_detail, name='move_detail'),
]
