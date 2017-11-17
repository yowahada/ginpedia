from django.shortcuts import render, get_object_or_404
from .models import Page

# Create your views here.
def blog_list(request):
	posts = Page.objects.filter(
            is_publick=True).reverse()
	return render(request, 'article/blog_list.html',{
		'posts': posts
	})

def blog_article(request, pk):
	posts = get_object_or_404(Page, pk=pk)
	return render(request, 'article/blog_detail.html',{
		'posts':posts
	})