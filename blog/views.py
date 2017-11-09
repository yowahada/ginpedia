from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import ContactForm
from django.http import HttpResponse
from django.http import Http404


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/gin_list.html', {
        'posts': posts
    })

def detail(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', {
        'post': posts
    })

def contact_add(request):
	if request.method == "POST" :
		form= ContactForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('blog:gin_list')
	else:
		form = ContactForm()
	return render(request, 'blog/contact_add.html',{
		'form':form
	})

def about(request):
	return render(request, 'blog/about_us.html', )