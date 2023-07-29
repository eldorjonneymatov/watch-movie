from django.shortcuts import render
from django.http import JsonResponse
from movie.models import Movie

def list_view(request):
    movies = Movie.objects.all()
    movies = list(movies.values())
    data = {
        'movies': movies
    }
    return JsonResponse(data)


def detail_view(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'id': movie.id,
        'name': movie.name,
        'description': movie.description,
        'is_active': movie.is_active
    }
    return JsonResponse(data)