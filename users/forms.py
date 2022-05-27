from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from users.models import MyUser, FilmUsersInfo
from captcha.fields import CaptchaField


clases_for_css = 'border border-primary form-control bg-dark text-warning'


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': clases_for_css, "placeholder": "Username"}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': clases_for_css}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': clases_for_css}))
    email = forms.EmailField(label='Email',
                             widget=forms.TextInput(attrs={'class': clases_for_css}))
    about_user = forms.CharField(label='О себе', widget=forms.Textarea(attrs={'rows': 10, 'cols': 60, 'class': 'border border-primary bg-dark text-warning'}))
    birth_date = forms.DateField(label='День Рождения', widget=forms.DateInput(attrs={'class': 'border border-primary bg-dark text-warning', "placeholder": "dd.mm.yyyy"}))
    age = forms.IntegerField(label='Возраст', widget=forms.NumberInput(attrs={'class': 'bg-dark border border-primary text-warning'}))
    captcha = CaptchaField()

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password1', 'password2', 'photo', 'birth_date', 'age', 'about_user', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = ('username', 'password', 'photo', 'birth_date', 'age', 'about_user')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class FilmListView(forms.ModelForm):
    class Meta:
        model = FilmUsersInfo
        fields = ('filmlist',)

    filmlist = forms.ChoiceField(label='', choices=FilmUsersInfo.FILMLIST, initial='',
                               widget=forms.Select(attrs={'class': 'form-select w-100 bg-dark text-danger my-2'}))

