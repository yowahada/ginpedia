"""contet_processor."""
from .models import Post, Botanicals, Genre

def common(request):
    context = {
        "gin_sort" : Post.objects.all(),
        "gin_sort_country": Post.objects.values('Country').distinct(),
        "gin_sort_genre": Genre.objects.all(),
        "botanicals_sort" : Botanicals.objects.all(),
    }
    return context