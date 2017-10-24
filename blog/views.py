from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import ContactForm
from django.http import HttpResponse

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'blog/gin_list.html',{
					  'posts':posts
				  })

def detail(request, pk):
	return render(request,'blog/detail.html',{
		'post':Post.objects.get(pk=pk)
		})

def contact(request):
	return render(request, 'blog/contact.html',)

def about(request):
	return render(request, 'blog/about_us.html',)