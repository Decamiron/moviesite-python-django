from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView

from main.models import Film
from users.forms import RegisterUserForm, LoginForm, FilmListView
from users.models import MyUser


class ProfileInfo(DetailView):
    model = MyUser
    template_name = 'users/profile.html'
    pk_url_kwarg = 'id'
    context_object_name = 'user'

    def post(self, request, id):
        user_films = MyUser.objects.get(id=id).filmusersinfo_set.get(film_id=self.request.POST['filmid'])
        user_films.series = self.request.POST["series"]
        user_films.save()
        return redirect('users:profile', id)

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FilmListView
        try:
            context['form'].base_fields['series'].initial = self.request.GET['filmlist']
            movilist = self.request.GET['filmlist']
        except:
            context['form'].base_fields['series'].initial = 'abandoned'
            movilist = 'abandoned'
        context['filminfo'] = Film.objects.filter(
            filmusersinfo__user_id=context['user'].id,
            filmusersinfo__series=movilist
        )
        return context


def published_list(request):
    model = MyUser.objects.get(id=request.user.id)
    model.is_published = not model.is_published
    model.save()
    return redirect('users:profile', request.user.id)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/RegisterPage.html'
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.photo = self.request.FILES
        user = form.save()
        login(self.request, user)
        return redirect('main:index')


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('main:index')


def logout_user(request):
    logout(request)
    return redirect('main:index')
