from django.shortcuts import render
from .models import Movie, Author, MovieInstance, Genre

# Create your views here.

def index(request):
    num_movies = Movie.objects.all().count()
    num_instance = MovieInstance.objects.all().count()

    disponibles = MovieInstance.objects.filter(status__exact='a').count()
    num_authors= Author.objects.all().count()

    return render(
        request,
        'index.html',
        context = {
            'num_movies': num_movies,
            'num_authors': num_authors,
            'num_instance': num_instance,
            'disponibles': disponibles
        }
    )