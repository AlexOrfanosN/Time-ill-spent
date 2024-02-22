from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Series


def series_main(request):
    series = Series.objects.all()
    return render(request, 'series/series_main.html', {'series': series})

def series_detail(request, series_id):
    serie = get_object_or_404(Series, pk=series_id)
    return render(request, 'series/series_detail.html', {'serie': serie})
