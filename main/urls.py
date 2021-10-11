from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *
app_name = 'main'
urlpatterns = [
    path('', FilmHome.as_view(), name='index'),
    path('about/', about, name='about'),
    path('movie/<slug:movie_slug>/', MovieDetail.as_view(), name='movie_detail'),
    path('change_list/<int:id>', change_list, name='change_list'),
    path('review/<int:pk>', CommentFilm.as_view(), name='comment_film'),
    path('search/', Search.as_view(), name='search'),
    path('filter/', GenreFilter.as_view(), name='filter'),
]
