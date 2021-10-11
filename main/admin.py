from django.contrib import admin
from main.models import Film, Genre, Series, Country


class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'poster_url', 'year')
    list_display_links = ('title', 'id')
    search_fields = ('title', 'description')
    list_filter = ('premiere', 'genre')
    prepopulated_fields = {"slug": ("title",)}


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name',)
    list_filter = ('name',)


class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name',)
    list_filter = ('name',)


admin.site.register(Film, FilmAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Series)
admin.site.register(Country, CountryAdmin)
