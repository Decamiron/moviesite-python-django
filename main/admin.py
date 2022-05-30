from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

from main.models import Film, Genre, Series, Country


class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'poster_url', 'year')
    list_display_links = ('title', 'id')
    search_fields = ('title', 'description')
    list_filter = ('premiere', 'genre')
    prepopulated_fields = {"slug": ("title",)}
    fields = (
        'title',
        'slug',
        'description',
        'poster_url',
        'year',
        'premiere',
        ('genre', 'country'),
        'series',
    )
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title',)
    list_filter = ('title',)


class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title',)
    list_filter = ('title',)


class SeriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Film, FilmAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Country, CountryAdmin)
