from django.contrib import auth
from django.db.models import Avg, Q
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DetailView, CreateView

import users.models
from main.forms import Comments
from main.models import Film, Genre, Country, Series
from users.forms import FilmListView
from users.models import FilmUsersInfo


class GenreCountry:
    def get_genres(self):
        return Genre.objects.all()

    def get_countries(self):
        return Country.objects.all()


class FilmHome(GenreCountry, ListView):
    model = Film
    template_name = 'index.html'
    context_object_name = 'films'
    paginate_by = 8

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['film_search'] = self.request.GET.get("film_search")
        return context


class MovieDetail(DetailView):
    model = Film
    template_name = 'main/film_detail.html'
    slug_url_kwarg = 'movie_slug'
    context_object_name = 'film'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['film_series'] = Film.objects.filter(series_id=context['film'].series_id).exclude(id=context['film'].id)
        context['form'] = Comments
        context['list_form'] = FilmListView
        try:
            context['series_name'] = context['film_series'].series.title
        except:
            context['series_name'] = ''
        context['rating'] = FilmUsersInfo.objects.filter(film_id=context['film'].pk).aggregate(res=Avg('rating'))
        return context


class CommentFilm(CreateView):
    form_class = Comments
    template_name = 'main/film_detail.html'
    model = users.models.FilmUsersInfo
    slug_field = 'movie_slug'

    def post(self, request, pk):
        user = auth.get_user(request)
        try:
            info = FilmUsersInfo.objects.get(film_id=pk, user_id=user.pk)
            info.rating = request.POST['rating']
            info.comment = request.POST['comment']
            info.save()
        except:
            FilmUsersInfo.objects.create(
                rating=request.POST['rating'],
                comment=request.POST['comment'],
                filmlist=FilmUsersInfo.none_list,
                film_id=pk,
                user_id=user.pk
            )

        return redirect('main:index')


class Search(FilmHome, ListView):
    def get_queryset(self):
        return Film.objects.filter(title__icontains=self.request.GET.get("film_search").capitalize())


class GenreFilter(GenreCountry, ListView):
    template_name = 'index.html'
    context_object_name = 'films'

    def get_queryset(self):
        queryset = Film.objects.filter(
            Q(genre__in=self.request.GET.getlist("genre")) & Q(
                country__in=self.request.GET.getlist("country"))).distinct()
        if len(queryset) == 0:
            queryset = Film.objects.filter(
                Q(genre__in=self.request.GET.getlist("genre")) | Q(
                    country__in=self.request.GET.getlist("country"))).distinct()
        return queryset

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['films'] = self.get_queryset()
        return context


def change_list(request, id):
    try:
        user_film = FilmUsersInfo.objects.get(user_id=request.user.id, film_id=id)
        user_film.filmlist = request.POST['filmlist']
    except FilmUsersInfo.DoesNotExist:
        user_film = FilmUsersInfo(filmlist=request.POST['filmlist'], user_id=request.user.id, film_id=id)

    user_film.save()
    return redirect('main:index')


def about(request):
    return render(request, 'main/about.html')


def pageNotFound(request, exception):
    return render(request, 'Error404.html')


def serverError(exception):
    return HttpResponse(f"<h1>Don't worry, there are only 500 reasons why this error could occur...</h1>")
