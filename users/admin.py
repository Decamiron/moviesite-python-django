from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register, ModelAdminGroup

from users.models import MyUser, FilmUsersInfo


class CustomUserAdmin(ModelAdmin):
    model = MyUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('photo', 'birth_date', 'age', 'bio', 'is_published')}),
    )
    list_display = ['username', 'email', 'photo', 'birth_date', 'age']


class FilmUsersInfoAdmin(ModelAdmin):
    model = FilmUsersInfo
    list_display = ['id', 'users_info', 'film_info', 'series', 'grade']
    search_fields = ['users_info__username', 'film_info__title']


class UserInfo(ModelAdminGroup):
    menu_label = 'Пользователи'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (FilmUsersInfoAdmin, CustomUserAdmin)


modeladmin_register(UserInfo)
