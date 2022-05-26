from django.contrib import admin
from wagtail.contrib.modeladmin.options import ModelAdminGroup, ModelAdmin, modeladmin_register

from main.models import Film, Genre, Series, Country


class FilmAdmin(ModelAdmin):
    model = Film
    list_display = ('id', 'title', 'poster_url', 'year')
    list_display_links = ('title', 'id')
    search_fields = ('title', 'description')
    list_filter = ('premiere_date', 'genre')
    # prepopulated_fields = {"slug": ("title",)}


class GenreAdmin(ModelAdmin):
    model = Genre
    # prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title',)
    list_filter = ('title',)


class CountryAdmin(ModelAdmin):
    model = Country
    # prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title',)
    list_filter = ('title',)


class SeriesAdmin(ModelAdmin):
    model = Series
    # prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title',)
    list_filter = ('title',)


class FilmInfo(ModelAdminGroup):
    menu_label = 'Фильмы'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 100  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (FilmAdmin, GenreAdmin, CountryAdmin, SeriesAdmin)


modeladmin_register(FilmInfo)
