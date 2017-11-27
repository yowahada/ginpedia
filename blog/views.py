from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import ContactForm
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, DetailView, ListView
from .models import Post, Botanicals
from article.models import Page

"""メインリスト"""
def post_list(request):
	posts = Post.objects.all().order_by('published_date').reverse()
	# 絞りこみ + オーダー
	# posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

	"""paginator"""
	page = request.GET.get('page',1)

	paginator = Paginator(posts,5)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	return render(request, 'blog/gin_list.html', {
        	'posts': posts
    	})

"""ジン詳細画面"""
def detail(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', {
        'post': posts
    })

"""form.py呼び出し"""
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



# """データ引渡しを手動で行う場合"""
# class MaterialsView(TemplateView):
# 	template_name = "blog/material.html"
#
# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		"""ここに処理記載"""
# 		return context

"""ボタニカル詳細画面/DetailView実装"""
class botanicalDetailView(DetailView):

	model = Botanicals
	# pk_url_kwarg = 'id'
	# template_name = 'blog/test.html'

	# urlに数字ではなく文字を入れる場合。urls.pyにも反映
	slug_field = "title"  # モデルのフィールドの名前
	slug_url_kwarg = "title"  # urls.pyでのキーワードの名前

"""filter、Search機能実装用view"""
class GinListView(ListView):

	model = Post
	context_object_name = "gin_list"
	paginate_by = 5

	def get_context_data(self, **kwargs):
		context = super(GinListView, self).get_context_data(**kwargs)
		# 最新の記事X件を抽出
		botanicals = Page.objects.all().order_by('id').reverse()[:3]
		context['botanicals'] = botanicals

		return context

	def get_queryset(self):
		# デフォルトは全件取得らしい
		results = self.model.objects.all()

		q_name = self.request.GET.get('name')

		if q_name is not None:
			results = results.filter(
				Q(title__icontains=q_name) | Q(Tasting_note__icontains=q_name) | Q(Country__icontains=q_name)
			)
		return results