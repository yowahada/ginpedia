from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Botanicals
from .forms import ContactForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, DetailView, ListView


# Create your views here.
def post_list(request):
	posts = Post.objects.all()
	#posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	page = request.GET.get('page',1)

	paginator = Paginator(posts,3)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

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



"""
データ引渡しを手動で行う場合
"""
# class MaterialsView(TemplateView):
# 	template_name = "blog/material.html"
#
# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		"""
# 		ここに処理記載
# 		"""
# 		# context['tag'] =
#
# 		return context

class botanicalDetailView(DetailView):

	model = Botanicals
	pk_url_kwarg = 'id'
	# template_name = 'blog/test.html'