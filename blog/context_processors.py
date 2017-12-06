"""contet_processor."""
from .models import Post, Botanicals

def common(request):
    context = {
        "gin_sort" : Post.objects.all(),
        "gin_sort_country": Post.objects.values('Country').distinct(),
        "botanicals_sort" : Botanicals.objects.all(),
    }
    return context
