from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies': [
        {
            'id': 1,
            'title': 'The Shawshank Redemption',
            'year': 1994,
            'director': 'Frank Darabont',
        },
        {
            'id': 2,
            'title': 'The Godfather',
            'year': 1972,
            'director': 'Francis Ford Coppola',
        },
        {
            'id': 3,
            'title': 'The Dark Knight',
            'year': 2008,
            'director': 'Christopher Nolan',
        },
    ]
}

def movies(request):
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse("Home page")