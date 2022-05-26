from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import MyUser, FilmUsersInfo


class CustomUserAdmin(admin.ModelAdmin):
    model = MyUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('photo', 'birth_date', 'age', 'about_user', 'is_published')}),
    )
    list_display = ['username', 'email', 'photo', 'birth_date', 'age']


class FilmUsersInfoAdmin(admin.ModelAdmin):
    model = FilmUsersInfo
    list_display = ['id', 'user', 'film', 'series', 'raiting']
    search_fields = ['users_info__username', 'film__title']


admin.site.register(MyUser, CustomUserAdmin)
admin.site.register(FilmUsersInfo, FilmUsersInfoAdmin)
