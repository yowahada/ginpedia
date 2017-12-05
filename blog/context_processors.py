"""contet_processor."""
from .models import Post, Botanicals

def common(request):
    context = {
        "gin_sort" : Post.objects.all(),
        "botanicals_sort" : Botanicals.objects.all(),
    }
    return context
