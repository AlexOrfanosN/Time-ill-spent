from django.db import models


class Genre(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type

class Series(models.Model):
    title = models.CharField(max_length=255)
    genre = models.ManyToManyField(Genre)
    image = models.ImageField(upload_to='series_images', null=True, blank=True)
    seasons = models.IntegerField(default=1)
    release_year = models.IntegerField(default=2022)
    quick_summary = models.TextField(max_length=1000, null=True, blank=True)  
    thoughts = models.TextField(max_length=10000, null=True, blank=True)      
    imdb_link = models.URLField(blank=True, null=True)

