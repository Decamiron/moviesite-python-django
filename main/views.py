from django.contrib import auth
from django.db.models import Avg, Q
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import *

import users.models
from main.forms import Comments
from main.models import *
from users.forms import FilmListView


class GenreCountry:
    def get_genres(self):
        return Genre.objects.all()

    def get_countrys(self):
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


def about(request):
    return render(request, 'main/about.html')


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
        context['raiting'] = users.models.FilmUsersInfo.objects.filter(film_info_id=context['film'].pk).aggregate(
            res=Avg('raiting'))
        return context


def change_list(request, id):
    print('ChangeList')
    try:
        a = users.models.FilmUsersInfo.objects.get(users_info_id=request.user.id, film_info_id=id)
        a.series = request.POST['series']
    except:
        a = users.models.FilmUsersInfo(series=request.POST['series'], users_info_id=request.user.id, film_info_id=id)
    finally:
        a.save()
    return redirect('main:index')


class CommentFilm(CreateView):
    form_class = Comments
    template_name = 'main/film_detail.html'
    model = users.models.FilmUsersInfo
    slug_field = 'movie_slug'

    def post(self, request, pk):
        user = auth.get_user(request)
        try:
            info = users.models.FilmUsersInfo.objects.get(film_info_id=pk, users_info_id=user.pk)
            info.raiting = request.POST['raiting']
            info.comment = request.POST['comment']
            info.save()
        except:
            users.models.FilmUsersInfo(raiting=request.POST['raiting'], comment=request.POST['comment'], film_info_id=pk, users_info_id=user.pk).save()

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


def pageNotFound(request, exception):
    return render(request, 'Error404.html')


def serverError(exception):
    return HttpResponse(f"<h1>Don't worry, there are only 500 reasons why this error could occur...</h1>")
