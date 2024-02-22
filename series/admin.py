from django import forms
from django.contrib import admin
from .models import Genre, Series


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')


class SeriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_genres', 'seasons', 'release_year')

    def display_genres(self, obj):
        return ", ".join([genre.type for genre in obj.genre.all()])

    display_genres.short_description = 'Genres'
    


admin.site.register(Genre, GenreAdmin)
admin.site.register(Series, SeriesAdmin)
